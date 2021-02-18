from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<slug:guess>', views.GameView.as_view()),
    path('choice/<int:option>', views.ChoiceView.as_view()),
    path('danger/<str:input>', views.DangerView.as_view()),
    path('simple', views.simple),
    path('guess', views.guess),
    path('special', views.special),
    path('nuts', views.nuts, name = 'nut'),
    path('loop', views.loop),
    path('nested', views.nested),
    path('nested_objects', views.nested_objects),
    path('inheritance1', views.Inheritance1.as_view()),
    path('inheritance2', views.Inheritance2.as_view()),
    path('urlmap', views.urlmap, name = 'url1')
]