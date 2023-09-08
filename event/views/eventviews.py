from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class CreateViewset(viewsets.ViewSet):
    permission_classes(IsAuthenticated)
    def create (self, request):
        created = True
        if created:
            return Response({'data': 'Create group succelly'}, status=status.HTTP_201_CREATED)
        return Response({'data':'Error create group'}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request):
        return Response({'data':'list event'})
    
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