from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def in_out_groupNotification(request):
    return Response({'data':'user notification, new user enter or out group'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def emailConfirmNotification(request):
    return Response({'data':'confirmation event 1h avant'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def userSubcribeEventNotification(request):
    return Response({'data':'notificate admin if user subcribe'})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def subscribeEventNotification(request):
    return Response({'data':'user add event '})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def newEventNotification(request):
    return Response({'data':'new event created'})