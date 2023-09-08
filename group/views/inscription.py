from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets,status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from account.models import CustomUser
from group.models import Group, Inscription
from django.db.models import Q
from group.serializer.inputSerializer import InscriptionSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def subscribe(request,idgroup=None,iduser=None):
    if request.method == 'POST':
        if iduser is not None:
            if idgroup is not None:
                user = CustomUser.objects.get(id=iduser)
                group = Group.objects.get(id=idgroup)         
                serializer = InscriptionSerializer(data=request.data)
                repetition = Inscription.objects.filter(Q(user_id=iduser) & Q(group_id=idgroup))
                if not repetition:
                    if serializer.is_valid():
                        serializer.save(group=group, user=user)
                        return Response({'data': 'Inscription réussie'}, status=status.HTTP_200_OK)
                    return Response({'data':'Echec d\'inscription'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'data': 'Déjà inscrit'}, status=status.HTTP_200_OK)
                
                
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def unsubscribe(request,idgroup=None,iduser=None):
    if request.method =='POST':
        if iduser is not None:
            if idgroup is not None:
                existe = Inscription.objects.filter(Q(user_id=iduser) & Q(group_id=idgroup))
                if existe:
                    existe.delete()
                    return Response({'data': 'désinscription réussie'}, status=status.HTTP_200_OK)
                return Response({'data': 'vous n\'etes pas inscrire'}, status=status.HTTP_200_OK)
                    
                    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def listMember(request, idgroup):
    group = Group.objects.get(id=idgroup)
    listMember = Inscription.objects.filter(group_id = group)
    userid = []
    for id in listMember:
        userid.append()
    return Response({'data1':'list member of groupe'})
    
@api_view(['GET'])   
@permission_classes([IsAuthenticated])
def numberMember(request):
    return Response({'data1':'number membre of groupe'})
    
# group list user on subscribe
@api_view(['GET'])  
@permission_classes([IsAuthenticated])
def myGroup(request):
    return Response({'data1':'my groupe'})