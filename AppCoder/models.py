from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User




class Game(models.Model):

    def __str__(self) :
        return f"{self.titulo}"

    titulo= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=70)
    genero= models.CharField(max_length=30)
    fecha_de_estreno= models.DateField()
    tipo_de_juego= models.CharField(max_length=60)
    caratula= models.ImageField(upload_to = 'juegos', null=TRUE, blank=TRUE)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return self.user.username