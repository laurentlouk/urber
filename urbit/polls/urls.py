from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^account/', views.account, name='account'),
    url(r'^profile/', views.profile, name='profile'),
]
