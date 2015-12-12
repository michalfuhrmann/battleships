from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import render_to_response, render

from battleships.user_services import user_login, user_register


def index(request):
    return render(request, "battleships/user/user.html")


def login(request):
    if request.method == 'GET':
        return render(request, "battleships/user/login.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if user_login(username, password):
            return HttpResponseRedirect('/battleships/main')
        return render(request, "battleships/user/login.html", {"error": 'Zly login/haslo'})


def register(request):
    if request.method == 'GET':
        return render(request, "battleships/user/register.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            error = 'Hasla nie pasuja'
        else:
            if user_register(username, password1):
                return HttpResponseRedirect('/battleships/login')
            error = 'Login zajety'
        return render(request, "battleships/user/register.html", {"error": error})


def main(request):
    return render(request, "battleships/user/main.html")
