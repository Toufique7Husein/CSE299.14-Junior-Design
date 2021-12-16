from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from django.forms import ModelForm



class SignupFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']
        
        #print(User.username)
        
    def __init__(self, *args, **kwargs):
        super(SignupFrom, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Name','required': 'required'}
        self.fields['username'].widget.attrs = {'class': 'form-control', 'placeholder': 'User Name','required': 'required'}
        self.fields['password1'].widget.attrs = {'class': 'form-control', 'placeholder': 'password','required': 'required'}
        self.fields['password2'].widget.attrs = {'class': 'form-control', 'placeholder': 'Confirm password','required': 'required'} 
        self.fields['email'].widget.attrs = {'class': 'form-control', 'placeholder': 'Email','required': 'required'}      

class EditProfile(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username','email', 'image', 'bio']
        
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control',
                                              'placeholder' : 'Name'
                                             }),
            'username' : forms.TextInput(attrs={'class' : 'form-control',
                                              'placeholder' : 'Write From Here'
                                              }),
            'email' : forms.TextInput(attrs={'class' : 'form-control',
                                              'placeholder' : 'email'
                                              }),
            
            'bio' : forms.Textarea(attrs={'class' : 'form-control',
                                              'placeholder' : 'bio'
                                              }),
        }
        