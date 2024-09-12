from django.db import models
from django.contrib.auth.models import User

# Modèle Donateur
class Donateur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    gs_rh = models.CharField(max_length=3)
    ville = models.CharField(max_length=100)
    telephone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.groupe_sanguin})"

# Modèle Hôpital
class Hopital(models.Model):
    nom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    capacite = models.IntegerField()
    specialite = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

# Modèle Médecin
class Medecin(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)

    def __str__(self):
        return f"Dr. {self.prenom} {self.nom}"

# Modèle Receveur
class Receveur(models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    gs_rh = models.CharField(max_length=3)
    hopital = models.ForeignKey(Hopital, on_delete=models.CASCADE)
    medecin = models.ForeignKey(Medecin, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.groupe_sanguin})"

# Modèle Poche de sang
class Poche(models.Model):
    numero_tubulaire = models.CharField(max_length=50, unique=True)
    gs_rh = models.CharField(max_length=3)
    quantite_ml = models.IntegerField()
    date_de_collecte = models.DateField()
    date_d_expiration = models.DateField()
    donateur = models.ForeignKey(Donateur, on_delete=models.CASCADE)
    receveur = models.ForeignKey(Receveur, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Poche {self.numero_tubulaire} - {self.groupe_sanguin}"
