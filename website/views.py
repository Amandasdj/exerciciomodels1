from django.shortcuts import render
from website.models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
       data = Pessoas()
       data.nome = request.POST['nome']
       data.sobrenome =request.POST['sobrenome']
       data.data_de_nascimento = request.POST['data_de_nascimento']
       data.cpf = request.POST['cpf']
       data.cep = request.POST['cep']
       data.item_de_doacao = request.POST['item_de_doacao']
       data.save()


   
    return render(request, 'index.html') 
def sobre(request):
  return render(request, 'Sobre.html') 