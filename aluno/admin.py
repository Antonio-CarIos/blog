from django.contrib import admin
from .models import Aluno, Curso

# Register your models here.
admin.site.register(Aluno)
class AlundoAdmin(admin.ModelAdmin):
    list_display = ('nome','email','telefone','habilidades', 'interesse','curso')

admin.site.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
