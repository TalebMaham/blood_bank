from rest_framework import serializers
from .models import Donateur, Hopital, Medecin, Receveur, Poche

class DonateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donateur
        fields = '__all__'

class HopitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hopital
        fields = '__all__'

class MedecinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medecin
        fields = '__all__'

class ReceveurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receveur
        fields = '__all__'

class PocheSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poche
        fields = '__all__'
