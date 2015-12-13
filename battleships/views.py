from django.http import HttpResponseRedirect
from django.shortcuts import render

from battleships.models import Game
from battleships.translations import get_translations, get_available_languages
from battleships.user_services import user_login, user_register, create_session, get_user_session, invalidate_session, \
    add_user_cookie, get_current_user, get_current_username_by_request, add_language_cookie, get_language_cookie

APP_USER = 'app_user'
LANGUAGES = 'app_languages'


def my_render(request, template, variables={}):
    variables.update(get_translations(get_language_cookie(request)))
    variables.update(get_available_languages())
    username = get_current_username_by_request(request)
    if username:
        variables[APP_USER] = username
    return render(request, template, variables)


def login_required(function):
    def wrapper(request, *args, **kwargs):
        if get_current_username_by_request(request):
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/battleships/login')

    return wrapper


def login(request):
    if request.method == 'GET':
        return my_render(request, "battleships/user/login.html")
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if user_login(username, password):
            response = HttpResponseRedirect('/battleships/main')
            add_user_cookie(response, create_session(username))
            return response
        return my_render(request, "battleships/user/login.html", {"error": 'Zly login/haslo'})


def logout(request):
    invalidate_session(get_user_session(request))

    return HttpResponseRedirect('/battleships/login')


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


def choose_language(request):
    origin_url = request.GET.get('return_url')
    if request.method == 'POST' and origin_url is not None:
        selected_language = request.POST['selected_language']
        response = HttpResponseRedirect(origin_url)
        add_language_cookie(response, selected_language)
        return response


def new_game(request):
    return my_render(request, "battleships/game/game.html")


def join_game(request):
    return my_render(request, "battleships/game/game.html")


def watch_game(request):
    return my_render(request, "battleships/game/game.html")


@login_required
def index(request):
    return my_render(request, "battleships/user/user.html")


@login_required
def main(request):
    return my_render(request, "battleships/user/main.html")


@login_required
def games(request):
    variables = {}
    variables['games'] = Game.objects.order_by('date')
    return my_render(request, "battleships/game/game_list.html", variables)


@login_required
def new_game(request):
    Game.objects.create(firstPlayer=get_current_user(request))
    return HttpResponseRedirect('/battleships/games')
