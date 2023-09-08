from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import viewsets,status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sendMessageEvent(request):
    return Response({'data':'send mssage sucess'}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listMessageEvent(request):
    return Response({'data':'list message '}, status=status.HTTP_202_ACCEPTED)