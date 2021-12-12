from django.http.response import HttpResponse
from django.shortcuts import render

from short_story.models import ShortStory

# Create your views here.
def home(request):
    #demo
    short_story = ShortStory.objects.all()
    context = {'short_story': short_story}
    return render(request, 'home.html', context)