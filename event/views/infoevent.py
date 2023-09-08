from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import viewsets,status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detailEvent(request):
    return Response({'data':'list  detail event'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listEvent(request):
    return Response({'data':'list event '}, status=status.HTTP_200_OK)