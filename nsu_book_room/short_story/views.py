from django.shortcuts import render
from .models import ShortStory

def short_story(request):
    shortStory = ShortStory.objects.all()
    context = {'short_story': shortStory}
    # for i in shortStory:
    #     print(i.title)
    return render(request, 'shortstory.html', context)


def readShortStory(request, pk):
    post = ShortStory.objects.get(id = pk)
    print(post.writer.username)
    context = {"read":post}
    return render(request, 'read_short_story.html', context)
    