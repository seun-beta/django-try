from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('get', views.getform, name='get'),
    path('post', views.postform, name='post'),
    path('get_try', views.get_try, name='get_try'),
    path('post_try', views.post_try, name='post_try')
]