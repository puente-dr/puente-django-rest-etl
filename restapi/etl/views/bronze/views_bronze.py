from django.contrib.auth.models import Group, User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets,response
from restapi.etl.models.bronze import HistoryenvironmentalhealthBronze

from restapi.etl.serializers.bronze import HistoryenvironmentalhealthBronzeSerializer



class HistoryenvironmentalhealthBronzeViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving raw Environmental Health records
    """
    queryset = HistoryenvironmentalhealthBronze.objects.all()

    def list(self, request):
        serializer = HistoryenvironmentalhealthBronzeSerializer(self.queryset, many=True)
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None):
        environmental_health_record = get_object_or_404(self.queryset, pk=pk)
        serializer = HistoryenvironmentalhealthBronzeSerializer(environmental_health_record)
        return response.Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     permission_classes = [permissions.IsAuthenticated]