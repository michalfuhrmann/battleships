from django.http import HttpResponseRedirect
from django.shortcuts import render

from battleships.user_services import user_login, user_register, create_session, get_logged_user

COOKIE_SESSION = 'session-cookie'


def my_render(request, template, variables={}):
    user_session = request.COOKIES.get(COOKIE_SESSION)
    if user_session:
        username = get_logged_user(user_session)
        variables['app_user'] = username if username else 'gosc'
    return render(request, template, variables)


def index(request):
    return my_render(request, "battleships/user/user.html")


def login(request):
    if request.method == 'GET':
        return my_render(request, "battleships/user/login.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if user_login(username, password):
            user_session = create_session(username)
            response = HttpResponseRedirect('/battleships/main')
            response.set_cookie(COOKIE_SESSION, user_session)
            return response
        return my_render(request, "battleships/user/login.html", {"error": 'Zly login/haslo'})


def register(request):
    if request.method == 'GET':
        return my_render(request, "battleships/user/register.html")
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
        return my_render(request, "battleships/user/register.html", {"error": error})


def main(request):
    return my_render(request, "battleships/user/main.html")


