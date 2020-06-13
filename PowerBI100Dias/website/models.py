from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Aula(models.Model):
    title = models.CharField(max_length=100)
    subTitle = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    aulaNumber = models.IntegerField()
    video = models.CharField(max_length=300)
    text = models.TextField()
    image = models.ImageField(upload_to='posts', null=True, blank=True)

    publicado = models.DateTimeField(default=timezone.now())
    cadastrado = models.DateTimeField(auto_now_add = True )
    alterado = models.DateTimeField(auto_now = True)

    ativado = models.BooleanField(default = True)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title + self.sub_title

class Comentario(models.Model):
    SEXO = (
        ('M', 'Maculino'),
        ('F', 'Feminino')
    )

    aulaCodigo = models.ForeignKey(Aula,on_delete = models.CASCADE)
    nameAutor = models.CharField(max_length=100)
    coment = models.TextField()
    ativado = models.BooleanField(default = True)
    publicado = models.DateTimeField(default=timezone.now())
    sexo = models.CharField(max_length = 10,
                              choices=SEXO,
                              default = 'M')

    def __str__(self):
        return self.coment