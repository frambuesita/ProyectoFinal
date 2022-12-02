from django.db import models

# Create your models here.
class Post(models.Model):
    post=models.CharField(max_length=200)
    fecha_de_creacion=models.DateField()

class Autor(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)

class Estilo(models.Model):
    estilo=models.CharField(max_length=40)

