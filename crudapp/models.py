from django.db import models


# Create your models here.
class Inscription(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.first_name


class Products(models.Model):
    nom = models.CharField(max_length=200)
    couleur = models.CharField(max_length=20)
    categorie = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=25, decimal_places=2)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nom} - {self.couleur}"
