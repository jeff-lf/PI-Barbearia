from django.shortcuts import render
from .models import Servico

def home(request):
    servicos = Servico.objects.all()
    return render(request, 'core/home.html', {'servicos': servicos})

# Create your views here.
