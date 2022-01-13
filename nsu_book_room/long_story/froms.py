from django.forms import ModelForm
from .models import LongStory
from django import forms

class LongStoryFrom(ModelForm):
    class Meta:
        model = LongStory
        fields = ['title', 'context']
       
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control',
                                              'placeholder' : 'Story Name'
                                             }),
            'context' : forms.Textarea(attrs={'class' : 'form-control',
                                              'placeholder' : 'Write From Here'
                                              }),
        }