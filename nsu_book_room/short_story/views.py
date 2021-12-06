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
        newmessage.save()
        return redirect('readShortStory', pk = post.id)
    comments = post.comment_set.all()
    context = {"read":post, "comment" : comments}
    return render(request, 'read_short_story.html', context)


@login_required(login_url='login')
def creatShortStory(request):
    froms = ShortStoryFrom()
    if request.method == 'POST':
        froms = ShortStoryFrom(request.POST)
        if froms.is_valid():
            froms.save()
            return redirect('home')
    context = {'from':froms}
    return render(request, 'shortstory_from.html', context)

def updateShortStory(request, pk):
    print(pk + "kkk")
    post = ShortStory.objects.get(id = int(pk))
    
    if request.method == 'POST':
        form = ShortStoryFrom(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ShortStoryFrom(instance=post)
    context = {'from' : form}
    return render(request, 'shortstory_from.html', context)
    