from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views import generic
from battleships.models import Question


def index(request):
    template = loader.get_template("battleships/user/user.html")
    context = RequestContext(request)
    return HttpResponse(template.render(context))


def index(request):
    return HttpResponse("hey")
