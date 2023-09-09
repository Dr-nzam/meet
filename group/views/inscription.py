from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets,status, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from account.models import CustomUser
from group.models import Group, Inscription
from django.db.models import Q
from group.serializer.inputSerializer import InscriptionSerializer
from account.serializers.userSerializers import UserSerializer
from group.serializer.inputSerializer import GroupSerialiser

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
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def listMember(request, idgroup = None):
    if idgroup is not None:
        if Group.objects.filter(id=idgroup).exists():
            group = Group.objects.get(id=idgroup)
            listMember = Inscription.objects.filter(group_id = group)
            userid = []
            member = []
            for id in listMember:
                userid.append(id.id)
            for iduser in userid:
                user = CustomUser.objects.get(id=iduser)
                member.append(user)
                serializers = UserSerializer(member, many=True).data
            return Response(serializers, status=status.HTTP_200_OK)
        return Response({'data':'group inconnu'}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])   
@permission_classes([IsAuthenticated])
def numberMember(request, idgroup=None):
    if idgroup is not None:
        if Group.objects.filter(id=idgroup).exists():
            group = Group.objects.get(id=idgroup)
            numberMember = Inscription.objects.filter(group_id = group).count()
            return Response({'numberMember':numberMember}, status=status.HTTP_200_OK)
    return Response({'data':'group inconnu'})
    
# group list user on subscribe
@api_view(['GET'])  
@permission_classes([IsAuthenticated])
def myGroup(request, iduser):
    myGroup = Inscription.objects.filter(user_id=iduser)
    idmygroup = []
    listgroup = []
    for mg in myGroup:
        idmygroup.append(mg.group.id)
    for id in idmygroup:
        group = Group.objects.get(id=id)
        listgroup.append(group)
        serializers = GroupSerialiser(listgroup, many=True).data
    return Response(serializers, status=status.HTTP_200_OK)