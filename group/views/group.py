from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets,status, serializers
from group.models import Group
from group.serializer.inputSerializer import GroupSerialiser
from rest_framework.response import Response

class GroupViewsets(viewsets.ViewSet):
    serializer_class = GroupSerialiser
    permission_classes = [IsAuthenticated]
    
    def create (self, request):
        serializer = GroupSerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'Create group succelly'}, status=status.HTTP_201_CREATED)
        print(serializer.errors) 
        return Response({'data':'Error create group'}, status=status.HTTP_400_BAD_REQUEST)
    
    # def list(self, request):
    #     search = request.GET.get("search", '')
    #     if search =='':
    #         groupList = Group.objects.all().order_by ('-id')
    #     else:
    #         groupList = Group.objects.filter(nomEvent__contains=search).order_by ('-id')
    #     serializer = GroupSerialiser(groupList, many=True).data
    #     return Response(serializer)
    
    # def retrieve(self, request, pk=None):
    #     id=pk
    #     if id is not None:
    #         EventParticulier = Evenement.objects.get(id=id)
    #         serializer = EventSerialiser(EventParticulier).data
    #         return Response(serializer)
    
    # def update (self, request,pk=None):
    #     try:
    #         instance = Evenement.objects.get(pk=pk)
    #     except Evenement.DoesNotExist:
    #         return Response({"error": "La ressource n'existe pas."}, status=404)

    #     serializer = EventSerialiser(instance, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=400)
        
    # def destroy(self, request, pk=None):
    #     EventParticulier = Evenement.objects.filter(pk=pk)
    #     EventParticulier.delete()
    #     return Response({'msg':'Évènement bien Supprimé'}, status= status.HTTP_202_ACCEPTED)
    