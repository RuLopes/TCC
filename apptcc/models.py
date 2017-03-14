# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Assuntos(models.Model):
    id_assunto = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'assuntos'


class Disciplinas(models.Model):
    id_disciplina = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'disciplinas'


class Perguntas(models.Model):
    id_pergunta = models.AutoField(primary_key=True)
    id_assunto = models.ForeignKey(Assuntos, models.DO_NOTHING, db_column='id_assunto')
    id_disciplina = models.ForeignKey(Disciplinas, models.DO_NOTHING, db_column='id_disciplina')
    id_alternativa_correta = models.CharField(max_length=20)
    descricao = models.CharField(max_length=2000)
    video_pergunta = models.FileField(upload_to = "apptcc/static/videos",blank=True)
    video_alternativa = models.FileField(upload_to = "apptcc/static/videos",blank=True)
    alternativa_a = models.CharField(max_length=2000, blank=True, null=True)
    alternativa_b = models.CharField(max_length=2000, blank=True, null=True)
    alternativa_c = models.CharField(max_length=2000, blank=True, null=True)
    alternativa_d = models.CharField(max_length=2000, blank=True, null=True)
    alternativa_e = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perguntas'
        unique_together = (('id_pergunta', 'id_assunto', 'id_disciplina'),)
