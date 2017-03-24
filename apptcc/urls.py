from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.inicio),
    url(r'^questoes/$',views.formulario_pesquisar_questoes),
    url(r'^inicio/$',views.novo_inicio),

]
