from django.shortcuts import render
from .models import *


def inicio(request):
    pergunta = Perguntas.objects.all()
    return render(request,'apptcc/inicio.html',{'pergunta': pergunta} )


def questoes(request):
    return render(request,'apptcc/questoes.html', )


def pesquisar(request, disciplina,assunto):
    post = get_object_or_404(Post, pk=pk,disciplina=disciplina,assunto=assunto)
    return render(request, 'blog/post_detail.html', {'post': post})


def formulario_pesquisar_questoes(request):
    if request.method == 'POST':
        if  request.POST.get('assunto') !='' and request.POST.get('disciplina') !='' :
            assunto = Assuntos.objects.get(descricao = request.POST.get('assunto','nao encontrado'))
            disciplina = Disciplinas.objects.get(descricao = request.POST.get('disciplina','nao encontrado'))
            pergunta = Perguntas.objects.filter(id_assunto = assunto.id_assunto,id_disciplina = disciplina.id_disciplina)
            return render(request,'apptcc/questoes.html',{'pergunta':pergunta})
        else:
            return render(request,'apptcc/questoes.html')
    else:
        return render(request,'apptcc/questoes.html')
