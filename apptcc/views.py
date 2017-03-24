

from django.shortcuts import render
from .models import *

#@type pergunta Perguntas


def inicio(request):
    pergunta = Perguntas.objects.all()
    return render(request,'apptcc/inicio.html',{'pergunta': pergunta} )

def novo_inicio(request):
    pergunta = Perguntas.objects.all()
    return render(request,'apptcc/novo_inicio.html',{'pergunta': pergunta} )


def questoes(request):
    return render(request,'apptcc/questoes.html', )


def pesquisar(request, disciplina,assunto):
    post = get_object_or_404(Post, pk=pk,disciplina=disciplina,assunto=assunto)
    return render(request, 'blog/post_detail.html', {'post': post})


#Falta validar as variaveis do formulario
def formulario_pesquisar_questoes(request):
    if request.method == 'POST':
        if  request.POST.get('assunto') != '' and request.POST.get('disciplina') != '' :

            try:
                disciplina = Disciplinas.objects.get(descricao = request.POST.get('disciplina','nao encontrado'))
            except Disciplinas.DoesNotExist:
                return render (request,'apptcc/questoes.html')

            try:
                assunto = Assuntos.objects.get(descricao = request.POST.get('assunto','nao encontrado'))
            except Assuntos.DoesNotExist:
                return render (request,'apptcc/questoes.html')

            pergunta = Perguntas.objects.filter(id_assunto = assunto.id_assunto,id_disciplina = disciplina.id_disciplina)

            return render (request,'apptcc/questoes.html',{'pergunta':pergunta})
        else:
            return render (request,'apptcc/questoes.html')
    else:
        return render (request,'apptcc/questoes.html')
