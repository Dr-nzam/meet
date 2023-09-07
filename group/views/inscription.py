from rest_framework.decorators import api_view, permission_classes, action
from rest_framework import viewsets,status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class Infogroup(viewsets.ViewSet):
    permission_classes(IsAuthenticated)
    
    @action(detail= False, methods=['POST'], name= 'subscribe', url_name='subscribe')
    def subscribe(self, request):
        inscription=True
        if inscription:
            return Response ({'data':'subscribe sucess'}, status=status.HTTP_200_OK)
        return Response({'data':'echec subscribe'}, status=status.HTTP_400_BAD_REQUEST)
    
    
    @action(detail= False, methods=['POST'], name= 'unsubscribe', url_name='unsubscribe')
    def unsubscribe(self, request):
        desincription = True
        if desincription:
            return Response ({'data':'unsubscribe sucess'}, status=status.HTTP_200_OK)
        return Response({'data':'echec unsubscribe'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail= False, methods=['GET'], name= 'listemember', url_name='liste-member-group')
    def listMember(self, request):
        return Response({'data1':'list member of groupe'})
    
    @action(detail= False, methods=['GET'], name= 'numbergroup', url_name='number-member-group')
    def numberMember(self, request):
        return Response({'data1':'number membre of groupe'})
    
    # group list user on subscribe
    @action(detail= False, methods=['GET'], name= 'listgroup', url_name='list-group-subscribe')
    def myGroup(self, request):
        return Response({'data1':'my groupe'})