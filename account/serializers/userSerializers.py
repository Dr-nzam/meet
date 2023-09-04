from rest_framework import serializers
from account.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id',
                  'first_name',
                  'last_name', 
                  'email', 
                  'username', 
                  'city', 
                  'centreInteret',
                  'password',
                  ]
        
    def create(self,validated_data):
        user = CustomUser(
            
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user