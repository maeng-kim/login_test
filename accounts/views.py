from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
import random



def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] ==request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1'],
            )
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('home')

def home(request):
        return render(request, 'lotto_index.html')


def lotto_index(request):
    return render(request, 'lotto_index.html')

def lotto_result(request):
    lotto_number = list()
    game = request.GET.get('game',1)
    pull_number = [index for index in range(1,46)]

    for _ in range(int(game)):
        lotto_number.append(random.sample(pull_number, 7))

    return render(request, 'lotto_result.html',{'lotto_number': lotto_number, 'game':game})
    


