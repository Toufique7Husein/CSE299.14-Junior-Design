from django.shortcuts import render

# Create your views here.
def login(request):
    # if(request.method == 'POST'):
    #     email = post['email']
    return render(request, 'login.html')

# def signun(request):
#    # return render(request, 'signup.html')

# def profile(request):
#    # return render(request, 'profile')

# def editProfile(request):
#     return render(request, 'profile', '')