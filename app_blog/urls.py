from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('inicio/', inicio, name='inicio'),
    path('publica/', PublicacaoView.as_view(), name='publica'),
    path('perfil/<str:nome>/', perfil, name='perfil'),

    path('comentario', comentario, name='comentario'),
]