from django import template
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.shortcuts import render_to_response,redirect
from django.views import generic
from battleships.models import Question


def index(request):
    template = loader.get_template("battleships/user/user.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def login(request):
    login_template = loader.get_template("battleships/user/login.html")
    context = RequestContext(request)
    return HttpResponse(login_template.render(context))


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/battleships/index')
    return render_to_response('battleships/user/login.html', context_instance=RequestContext(request))
