from rest_framework import serializers


class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    redirect_url = serializers.CharField(max_length=500, required=False)
    class Meta:
        fields = ['email']
        
class SetNewPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)
    password = serializers.CharField(max_length=68, write_only=True)
    confirmPassword = serializers.CharField(max_length=68, write_only=True)
    otp = serializers.CharField()
    class Meta:
        fields = ['password', 'confirmPassword','otp']

class ChangePasswordSerializer(serializers.Serializer):
    oldPassword = serializers.CharField(max_length=30)
    newPassword = serializers.CharField(max_length=30)
    
class GoogleLoginSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.CharField(max_length=30)
    # picture = serializers.CharField(max_length=255, allow_blank=True)