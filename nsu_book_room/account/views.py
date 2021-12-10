from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout
from .froms import SignupFrom
from .models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passward = request.POST['password']
        print(username)
        print(passward)
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'does not exist')
        
        user = authenticate(request, username = username, password = passward)
        
        if user is not None:
            user_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "wrong password")
    context = {}
    return render(request, 'login.html', context)


def signup(request):
    form = SignupFrom()
    print(request.method)
    if request.method == 'POST':
        form = SignupFrom(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
           # messages(request, 'an error occurs during the registration!')
           return redirect('home')
    context = {'form' : form}
    return render(request, 'signup.html', context)



def user_logout(request):
    logout(request)
    return redirect('home')

