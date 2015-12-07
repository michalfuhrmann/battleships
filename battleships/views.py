from django.http import HttpResponse
from django.template import loader, RequestContext
from django.views import generic
from battleships.models import Question

class DetailsView ( generic.DetailView):
    model = Question
    template_name = "test.html"

def index(request):
    tescik = "what is life "
    template = loader.get_template("test.html")
    context = RequestContext(request, {
        'tescik': tescik
    })
    return HttpResponse(template.render(context))
