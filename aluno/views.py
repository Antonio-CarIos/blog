from django.shortcuts import render, get_object_or_404
from .models import Aluno, Curso

# Create your views here.
def home(request):
    cursos = Curso.objects.all()
    
    context = {
        'cursos' : cursos
    }

    return render (
        request,
        'aluno/index.html',
        context
    )

def detalhes(request, pk):
    alunos = get_object_or_404(Aluno, pk=pk)

    context = {
        'aluno' : alunos
    }

    return render (
        request,
        'aluno/detalhes.html',
        context
    )

