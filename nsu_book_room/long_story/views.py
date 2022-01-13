from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .models import LongStory, Comment_LongStory
from .froms import LongStoryFrom
from django.contrib.auth.decorators import login_required

def long_story(request):
    shortStory = LongStory.objects.all()
    context = {'short_story': shortStory}
    return render(request, 'longstory.html', context)


def readLongStory(request, pk):
    post = LongStory.objects.get(id = pk)
    if request.method == 'POST':
        newmessage =  Comment_LongStory.objects.create(
            user = request.user,
            post = post,
            body = request.POST.get('body')
        )
      #  print(request.user.id)
        newmessage.save()
        return redirect('readLongStory', pk = post.id)
    comments = post.comment_longstory_set.all()
    context = {"i":post, "comment" : comments}
    return render(request, 'read_long_story.html', context)


@login_required(login_url='login')
def creatLongStory(request):
    page = "add"
    froms = LongStoryFrom()
    if request.method == 'POST':
        froms = LongStoryFrom(request.POST)
        if froms.is_valid():
            post = froms.save(commit = False)
            post.writer = request.user
            post.save()
            return redirect('longstory')
    context = {'from':froms, 'page' : page}
    return render(request, 'longstory_form.html', context)

def updateLongStory(request, pk):
   # print(pk + "kkk")
    page = "edit"
    post = LongStory.objects.get(id = int(pk))
    if request.method == 'POST':
        form = LongStoryFrom(request.POST, instance=post)
        if form.is_valid():
            temp = form.save(commit = False)
            temp.writer = request.user
            temp.save()
            return redirect('longstory')
    form = LongStoryFrom(instance=post)
    context = {'from' : form, 'page' : page}
    return render(request, 'longstory_form.html', context)
    