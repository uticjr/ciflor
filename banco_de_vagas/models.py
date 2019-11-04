from django.db import models


# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    descricao = models.TextField()
    foto = models.ImageField(upload_to='vagas_fotos', null=True, blank=True)
    empresa = models.ForeignKey(Empresa, models.CASCADE)

    def __str__(self):
        return self.empresa.nome

