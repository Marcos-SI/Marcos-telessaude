from django.shortcuts import render
from django.http import HttpResponse, Http404
import json
import os
from django.conf import settings

def carregar_noticias():
    json_path = os.path.join(settings.BASE_DIR,'tsac','data','tsac','base.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
def Home(request):
    noticias = carregar_noticias()

    return render(request,'tsac\pages\home.html',{
        'name':'Notícias – TelessaúdeAC',
        'noticia':noticias,
        'is_detail_page': False})
def noticia(request,id):
    noticias = carregar_noticias()
    noticia_selecionada = None
    for noticia in noticias:
        if noticia['id'] == id:
            noticia_selecionada = noticia
            break
    if not noticia_selecionada:
        raise Http404("Noticia Não encontrada")
    
    return render(request, 'tsac\partials\noticias.html', context={
        'name': 'Notícias – TelessaúdeAC',
        'is_detail_page': True,
        'noticia': noticia_selecionada})

# Create your views here.
