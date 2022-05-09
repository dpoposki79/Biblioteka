from rest_framework import serializers
from .models import Knigi, Clenovi

class KnigiSerilizer(serializers.ModelSerializer):
    class Meta:
        model=Knigi
        fields = "__all__"

class ClenoviSerilizer(serializers.ModelSerializer):
    naslov_kniga = serializers.SerializerMethodField()
    avtor_kniga = serializers.SerializerMethodField()
    class Meta:
        model=Clenovi
        fields = "__all__"
        read_only_fields= ("Pozajmena_kniga",)

    def create(self, validated_data):   #Ova se pravi koga se koristi POST metod
        return Knigi.objects.create(**validated_data)

    def create(self, validated_data):  
        return Clenovi.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

    def get_naslov_kniga(self, obj):
        if obj.Pozajmena_kniga != None:
            return obj.Pozajmena_kniga.Naslov
        else:
            return "Nema Pozajmeno"
    
    def get_avtor_kniga(self, obj):
        if obj.Pozajmena_kniga != None:
            return obj.Pozajmena_kniga.Avtor
        else:
            return "Nema Pozajmeno"