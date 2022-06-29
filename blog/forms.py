from django import forms

from .models import Valoracio

#form per votar estrelletes associat a model valoració
#per validació a view 'votar' i per renderitzar choises a template 'detail'
class VotaForm(forms.ModelForm):

    class Meta:
        model = Valoracio
        fields = (
            'valor',
        )
        
        widgets = {
            'valor': forms.RadioSelect(),
        }

        error_messages = {
            'valor': {
                'required': "NO HAS VOTAT!",
            },
        }