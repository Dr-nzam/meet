from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import viewsets,status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class MessageGroup(viewsets.ViewSet):
    
    permission_classes(IsAuthenticated)
    
    @action(detail=False, methods='POST', name='sendmessage', url_name='send-message')
    def sendMessageGroup(self, request):
        return Response({'data':'send mssage sucess'}, status=status.HTTP_202_ACCEPTED)
    
    
    @action(detail=False, methods='GET', name='list-message', url_name='list-message')
    def listMessageGroup(self, request):
        return Response({'data':'send mssage sucess'}, status=status.HTTP_202_ACCEPTED)