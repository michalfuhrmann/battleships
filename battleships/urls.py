from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url("^login/$", views.login, name="login"),
    url("^index/$", views.index, name="index")

]
