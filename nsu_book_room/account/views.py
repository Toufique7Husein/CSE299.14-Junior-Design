from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        passward = request.POST['password']
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


def signun(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            messages(request, 'an error occurs during the registration!')
    context = {'form':form}
    return render(request, 'signup.html', context)

# def profile(request):
#    # return render(request, 'profile')

# def editProfile(request):
#     return render(request, 'profile', '')



def user_logout(request):
    logout(request)
    return redirect('home')

