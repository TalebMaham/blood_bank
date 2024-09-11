from rest_framework import viewsets
from .models import Donateur, Hopital, Medecin, Receveur, Poche
from .serializers import DonateurSerializer, HopitalSerializer, MedecinSerializer, ReceveurSerializer, PocheSerializer

class DonateurViewSet(viewsets.ModelViewSet):
    queryset = Donateur.objects.all()
    serializer_class = DonateurSerializer

class HopitalViewSet(viewsets.ModelViewSet):
    queryset = Hopital.objects.all()
    serializer_class = HopitalSerializer

class MedecinViewSet(viewsets.ModelViewSet):
    queryset = Medecin.objects.all()
    serializer_class = MedecinSerializer

class ReceveurViewSet(viewsets.ModelViewSet):
    queryset = Receveur.objects.all()
    serializer_class = ReceveurSerializer

class PocheViewSet(viewsets.ModelViewSet):
    queryset = Poche.objects.all()
    serializer_class = PocheSerializer
