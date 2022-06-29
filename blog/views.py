from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone

from datetime import datetime, timedelta

from django.db.models import Avg
from .models import Post, Valoracio

from .forms import VotaForm

def post_list(request):
    #__lte -> menys o igual que
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    #post = get_object_or_404(Post, pk=post_id)
    
    #si no existeix post, template 404
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, 'blog/404.html')

    #nou form i per passar a template per renderitzar choices
    form = VotaForm()

    return render(request, 'blog/post_detail.html', {'post': post,'form': form })

"""
def vote(request, pk):
    return HttpResponse("You're voting on question %s." % pk)
"""

def votar(request, post_id):

    #post = get_object_or_404(Post, pk=post_id)
    #print(post)
    #print(post.id)
    #valor = request.POST['valor']
    #print(valor)

    #si no existeix post, template 404
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, 'blog/404.html')
    
    #si mètode POST
    if request.method == "POST":
        
        #nou form i li passem request per validació
        form = VotaForm(request.POST)
        print(form)
        print(form.is_valid())

        #si form vàlid
        if form.is_valid():
            #valor = request.POST['valor']
            #return HttpResponse("You're voting %s on question %s." % (valor, post_id) )

            #guardem form vinculat a objecte model valoracio
            #només guarda 'valor', amb commit false, no fa save model
            valoracio = form.save(commit=False)

            #completem camps model
            valoracio.post = post
            valoracio.data = timezone.now()

            #guardem model
            valoracio.save()

            #mitja en post.valoracions ?
            print(Valoracio.objects.filter(post=post_id).count())
            print(Valoracio.objects.filter(post=post_id).aggregate(Avg('valor')))

            nova_mitja = Valoracio.objects.filter(post=post_id).aggregate(Avg('valor'))
            post.valoracio_mitja = nova_mitja['valor__avg']
            post.save()

            #return redirect('post_detail', post_id)
            ok = 'GRÀCIES PEL TEU VOT :)'
            return render(request, 'blog/post_detail.html', {'post': post, 'form': form,'ok': ok })

        else:
            #return HttpResponse("CASTANYA!!!")
            return render(request, 'blog/post_detail.html', {'post': post,'form': form })
    else:
        return render(request, 'blog/404.html')

def post_results(request, post_id):

    #post = get_object_or_404(Post, pk=post_id)
    
    #si no existeix post, template 404
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return render(request, 'blog/404.html')
    
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % post_id)
    return render(request, 'blog/post_results.html', {'post': post})


def results(request):
    #response = "You're looking general results"
    #return HttpResponse(response)
    
    # amb - order by desc
    posts = Post.objects.order_by('-valoracio_mitja')
    print(posts)
    return render(request, 'blog/results.html', {'posts': posts})

def postquery(request):
    #response = "You're looking general results"
    #return HttpResponse(response)

    #posts = Post.objects.all

    # amb - order by desc
    # amb timedelta filtre per últims 'dies'
    cinc = Post.objects.filter(created_date__gte=datetime.now()-timedelta(days=5)).order_by('-created_date')
    print(cinc)
    
    millors = Post.objects.filter(valoracio_mitja__gte=3).order_by('-valoracio_mitja')
    print(millors)

    pitjors = Post.objects.filter(valoracio_mitja__lt=3).order_by('valoracio_mitja')
    print(pitjors)
    
    return render(request, 'blog/post_query.html', {
        'cinc': cinc,
        'millors': millors,
        'pitjors': pitjors,
        })

