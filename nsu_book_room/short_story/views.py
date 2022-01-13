from django.shortcuts import redirect, render
from .models import ShortStory, Comment
from .froms import ShortStoryFrom
from django.contrib.auth.decorators import login_required

def short_story(request):
    shortStory = ShortStory.objects.all()
    context = {'short_story': shortStory}
    # for i in shortStory:
    #     print(i.title)
    return render(request, 'shortstory.html', context)


def readShortStory(request, pk):
    post = ShortStory.objects.get(id = pk)
    if request.method == 'POST':
        newmessage = Comment.objects.create(
            user = request.user,
            post = post,
            body = request.POST.get('body')
        )
      #  print(request.user.id)
        newmessage.save()
        return redirect('readShortStory', pk = post.id)
    comments = post.comment_set.all()
    context = {"i":post, "comment" : comments}
    return render(request, 'read_short_story.html', context)


@login_required(login_url='login')
def creatShortStory(request):
    page = "add"
    froms = ShortStoryFrom()
    if request.method == 'POST':
        froms = ShortStoryFrom(request.POST)
        if froms.is_valid():
            post = froms.save(commit = False)
            post.writer = request.user
            post.save()
            return redirect('home')
    context = {'from':froms, 'page' : page}
    return render(request, 'shortstory_from.html', context)

def updateShortStory(request, pk):
   # print(pk + "kkk")
    page = "edit"
    post = ShortStory.objects.get(id = int(pk))
    if request.method == 'POST':
        form = ShortStoryFrom(request.POST, instance=post)
        if form.is_valid():
            temp = form.save(commit = False)
            temp.writer = request.user
            temp.save()
            return redirect('home')
    form = ShortStoryFrom(instance=post)
    context = {'from' : form, 'page' : page}
    return render(request, 'shortstory_from.html', context)
    