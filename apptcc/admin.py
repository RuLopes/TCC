from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import *

admin.site.register(Assuntos)
admin.site.register(Disciplinas)
admin.site.register(Perguntas)
