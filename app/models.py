from tkinter import CASCADE
from django.db import models

# Create your models here.

class Knigi(models.Model):
    Naslov = models.CharField(max_length=50, unique=True) 
    Avtor = models.CharField(max_length=50) 
    Zarn = models.CharField(max_length=50) 
    Godina = models.IntegerField()
    Kolicina = models.IntegerField()
    Lokacija = models.CharField(max_length=50) 
    Izdavac = models.CharField(max_length=50) 
    Jazik = models.CharField(max_length=50) 
    Strani = models.IntegerField()
    El_ver = models. BooleanField()
    El_path = models.FileField(null=True, blank=True)
    ISBN = models.CharField(max_length=50)
    Naslov_original = models.CharField(max_length=50, null=True)
    Nabavna_cena = models.FloatField()
    Kaznena_cena = models.FloatField()
    Prevedena = models.BooleanField()


class Clenovi(models.Model):
    Ime = models.CharField(max_length=30) 
    Prezime = models.CharField(max_length=30) 
    Data_clenstvo = models.DateField()
    Broj_clenska = models.IntegerField(unique=True)
    Telefon = models.CharField(max_length=20)
    Adresa = models.CharField(max_length=50)
    Data_ragjanje = models.DateField()
    Aktiven = models.BooleanField()
    Data_platena_clenarina = models.DateField()
    Dali_ima_pozajmeno = models. BooleanField()
    Pozajmena_kniga = models.ForeignKey(Knigi, on_delete=models.CASCADE, null=True, blank=True) #ForeignKey se koristi za relacija. Cascade e ako se izbrise knigata od Knigi da se izbrise i od kaj clenot sto ja ima pozajmento
    Email = models.CharField(max_length=50, null=True)
    Data_pozajmuvanje = models.DateTimeField(null=True, blank=True)
    denovi_potsetuvanje = models.IntegerField(null=True)