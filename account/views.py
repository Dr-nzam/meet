from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from account.serializers.userSerializers import UserSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from account.models import CustomUser
from account.serializers.inputSerializer import LoginSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def login(request):
    if request.method =='POST':
        email = request.data.get('email')
        password = request.data.get('password')
            
        try:
            account = CustomUser.objects.get(email=email)
        except:
            account = get_object_or_404(CustomUser, email=email)
                
        if not account:
            user = authenticate(email =email, password=password)
            if user :
                token, _ = Token.objects.get_or_create(user=user)
                serializer = UserSerializer(account, many=False)
                data = serializer.data
                data['token'] = token.key
                return Response(token, status=status.HTTP_200_OK)