from rest_framework import serializers
from account.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
    def create(self,validated_data):
        user = CustomUser(
            
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user