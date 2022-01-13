from django.shortcuts import render
from account.models import User

# Create your views here.
def discussion_home(request):
    user = User.objects.all()
    context = {user : 'user'}
    return render(request, 'discussion.html', context)
