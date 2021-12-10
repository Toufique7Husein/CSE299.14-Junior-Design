from django.forms import ModelForm
from .models import ShortStory
from django import forms

class ShortStoryFrom(ModelForm):
    class Meta:
        model = ShortStory
        fields = ['title', 'context']
       
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'context' : forms.Textarea(attrs={'class' : 'form-control'}),
        }
        
        
    