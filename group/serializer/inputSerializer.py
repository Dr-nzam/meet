from rest_framework import serializers
from group.models import Group,Inscription

class GroupSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        
        
class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'