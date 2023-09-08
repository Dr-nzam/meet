from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe(request):
    inscription=True
    if inscription:
        return Response ({'data':'subscribe sucess'}, status=status.HTTP_200_OK)
    return Response({'data':'echec subscribe'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unsubscribe(request):
    desincription = True
    if desincription:
        return Response ({'data':'unsubscribe sucess'}, status=status.HTTP_200_OK)
    return Response({'data':'echec unsubscribe'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def myEventSubscribe(request):
    return Response ({'data':'list my event subscribe'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def eventPast(request):
    return Response({'data':'list event pass'})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listEventGroup(request):
    return Response({'data':'list all event in group'})