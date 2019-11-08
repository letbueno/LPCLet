from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import PublicacaoForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as teste, logout as brabor, authenticate
from django.core.paginator import Paginator



def inicio(request):
    publicacoes = Publicacao.objects.all().order_by('data').reverse()
    usuarios = User.objects.all().order_by('-id')[0:30]

    return render(request, 'app_blog/inicio.html', {'publicacoes': publicacoes, 'usuarios':usuarios})

def perfil(request, nome):
    try:
        pessoa = User.objects.get(username=nome)
        publicacoes = Publicacao.objects.filter(autor=pessoa).order_by('-id')[0:30]

    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')

    return render(request, 'app_blog/perfil.html', {'publicacoes': publicacoes})
def comentario(request):
    return render(request, 'app_blog/comentario.html')
def DetalhePub(request, id_publicacao):
    try:
        pub = Publicacao.objects.get(pk=id_publicacao)
        comentario = Comentario.objects.filter(publicacao=pub)
    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')

    return render(request, 'app_blog/detalhe.html', {'pub': pub, 'comentario': comentario})



class PublicacaoView(FormView):
    template_name = 'app_blog/publica.html'
    form_class = PublicacaoForm

    def form_valid(self, form):
        dados = form.clean()
        pessoa = User.objects.get(username=self.request.user.username)
        publicacao = Publicacao(texto=dados['texto'], autor=pessoa)
        publicacao.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inicio')



class HomePageView(TemplateView):
    template_name = 'app_blog/inicio.html'