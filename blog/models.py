from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    valoracio_mitja = models.DecimalField(max_digits=5, decimal_places=2,default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Valoracio(models.Model):

    #per choises valors del 4 al 1, cal tupla index,valor
    #decreixent per css rating
    VALORS = [(i,i) for i in range(4,0,-1)]

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    data = models.DateTimeField(default=timezone.now)
    valor = models.IntegerField(default=0, choices=VALORS)
    
    def __str__(self):
        return str(self.data)
