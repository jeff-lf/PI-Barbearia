# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Importando o login_required
from .models import Servico, Agendamento
from .forms import AgendamentoForm

def home(request):
    return render(request, 'core/home.html')

def servicos(request):
    servicos = Servico.objects.all()
    return render(request, 'core/servicos.html', {'servicos': servicos})

@login_required
def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.usuario = request.user
            agendamento.save()
            return redirect('home')
    else:
        form = AgendamentoForm()
    return render(request, 'core/agendar.html', {'form': form})

def listar_agendamentos(request):
    agendamentos = Agendamento.objects.filter(usuario=request.user)
    return render(request, 'core/agendamentos.html', {'agendamentos': agendamentos})

