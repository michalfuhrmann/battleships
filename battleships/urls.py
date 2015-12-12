from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url("^login/$", views.login, name="login"),
    url("^register/$", views.register, name="register"),
    url("^index/$", views.index, name="index"),
    url("^main/$", views.main, name="main"),
]
