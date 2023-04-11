from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo=models.CharField(max_length=50)
    editorial=models.CharField(max_length=50)
    paginas=models.IntegerField()

class Biblioteca(models.Model):
    nombre=models.CharField(max_length=50)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()

class Autor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.CharField(max_length=50)
