from django.forms import ModelForm

from .models import ShortStory

class ShortStoryFrom(ModelForm):
    class Meta:
        model = ShortStory
        fields = '__all__'
        
    