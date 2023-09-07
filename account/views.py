from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from account.function.checkToken import expires_in, token_expire_handler
from account.function.sendEmail import sendMail
from account.serializers.userSerializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from account.models import CustomUser
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import check_password
from account.serializers.inputSerializer import ChangePasswordSerializer, GoogleLoginSerializer, ResetPasswordEmailRequestSerializer, SetNewPasswordSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import update_last_login
from account.authentication import ExpiringTokenAuthentication


@api_view(['POST'])
@authentication_classes([ExpiringTokenAuthentication])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([ExpiringTokenAuthentication])
def login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            account = CustomUser.objects.get(email=email)
        except:
            account = get_object_or_404(CustomUser, email=email)
        if account:
            user = authenticate(email=email, password=password)
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                token = token_expire_handler(token)
                serializer = UserSerializer(account, many=False)
                data = serializer.data
                data['expired_in'] = expires_in(token)
                data['token'] = token.key
                update_last_login(None, account)
                return Response(data, status=status.HTTP_200_OK)
            return Response({'data': 'Erreur to connected'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@authentication_classes([ExpiringTokenAuthentication])        
def reset_password_email(request):
        serializer = ResetPasswordEmailRequestSerializer(data=request.data)
        if serializer.is_valid():
            # user:CustomUser = CustomUser.objects.get(email=serializer.data["email"])
            # if user.is_google or user.is_facebook:
            #     return Response({"detail": "this account can't reset his password"}, status=status.HTTP_400_BAD_REQUEST)
            sendMail(serializer.data['email'])
            return Response({"detail": "email sent successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@authentication_classes([ExpiringTokenAuthentication])
def reset_password(request):
        serializer = SetNewPasswordSerializer(data=request.data)
        
        if serializer.is_valid():
            email = serializer.data['email']
            otp = serializer.data['otp']
            users = CustomUser.objects.filter(email=email)
            if not users.exists():
                return Response({"details":"Invalid email"}, status=status.HTTP_400_BAD_REQUEST)
            
            if users[0].otp !=otp:
                return Response({"details":"Wrong otp"}, status=status.HTTP_400_BAD_REQUEST)
            
            # if not password_check(request.data["password"]):
            #     return Response({"detail": "your password is too weak"}, status=status.HTTP_400_BAD_REQUEST)
            
            if  request.data["password"] != request.data['confirmPassword']:
                return Response({"detail": "Password do not match "}, status=status.HTTP_400_BAD_REQUEST)
            
            if  users[0].is_active != False:
                return Response({"detail": "Password do not match "}, status=status.HTTP_400_BAD_REQUEST)
           
            user:CustomUser = users.first()
            user.password = make_password(request.data["password"])
            user.is_active = True
            user.save()
            return Response({"detail": "password reset successfully"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
@authentication_classes([ExpiringTokenAuthentication])
@permission_classes([IsAuthenticated])
def change_password(request):
    serializer = ChangePasswordSerializer(data=request.data)
    if serializer.is_valid():
        if not check_password(serializer.data['oldPassword'], request.user.password):
            return Response({"detail": "wrong old password"}, status=status.HTTP_400_BAD_REQUEST)
        
        # if not password_check(serializer.data['newPassword']):
        #     return Response({"detail": "password is too weak"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = get_object_or_404(CustomUser, pk=request.user.pk)
        user.set_password(serializer.data["newPassword"])
        token, _ = Token.objects.get_or_create(user = request.user)
        token.delete()
        user.save()
        return Response({"detail": "password updated successfuly"}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([ExpiringTokenAuthentication])
def google_connexion(request):
    google_serializer = GoogleLoginSerializer(data=request.data["google"])
    
    if google_serializer.is_valid():
        
        if CustomUser.objects.filter(email=google_serializer.data["email"]).exists():
        
            if CustomUser.objects.filter(email=google_serializer.data["email"]).exists():
                try:
                    account = CustomUser.objects.get(email=google_serializer.data["email"])
                except:
                    account = get_object_or_404(CustomUser, email=google_serializer.data["email"])
        
            if account.is_active:
                token, _ = Token.objects.get_or_create(user = account)
                serializer = UserSerializer(account, many=False)
                data = serializer.data
                data['token'] = token.key
                return Response(data, status=status.HTTP_200_OK) 