from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()

class CategoriaNegocio(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    redirectTo = models.CharField(max_length=200)

class Panaderia(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50) 
    redirectTo = models.CharField(max_length=200)   
    image = models.CharField(max_length=70)

class Supermercado(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50) 
    redirectTo = models.CharField(max_length=200)   
    image = models.CharField(max_length=70)

class Restaurante(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50) 
    redirectTo = models.CharField(max_length=200)   
    image = models.CharField(max_length=70)

   