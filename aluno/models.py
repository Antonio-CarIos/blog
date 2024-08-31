from django.db import models

# Create your models here.

class Curso(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    image = models.ImageField(upload_to='capas/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    habilidades = models.TextField()
    interesses = models.TextField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='perfis/', null=True, blank=True)

    def __str__(self):
        return self.nome
    
