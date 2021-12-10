from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

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
