from django.db.models import Count

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from restapi.etl.models.bronze import HistoryenvironmentalhealthBronze

from restapi.etl.serializers.bronze import HistoryenvironmentalhealthBronzeSerializer

"""
list /environmentalhealthbronze/
create /environmentalhealthbronze/new/
detail /environmentalhealthbronze/1/
update /environmentalhealthbronze/1/edit/
delete /environmentalhealthbronze/1/delete/
any methods not dependent on an object /environmentalhealthbronze/view-name/
any methods dependent on a particular object /environmentalhealthbronze/1/view-name/
"""

class HistoryenvironmentalhealthBronzeViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving raw Environmental Health records
    """
    queryset = HistoryenvironmentalhealthBronze.objects.all()

    def list(self, request):
        serializer = HistoryenvironmentalhealthBronzeSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        environmental_health_record = get_object_or_404(self.queryset, pk=pk)
        serializer = HistoryenvironmentalhealthBronzeSerializer(environmental_health_record)
        return Response(serializer)
    
    @action(detail=False, methods=['post'])
    def get_count(self, request, pk=None):
        fields = request.data.get('fields', [])
        field = fields[0]
        queryset = HistoryenvironmentalhealthBronze.objects.values(field).annotate(count_of_unique_values=Count('*')).order_by("-count_of_unique_values")
        return Response(queryset)


    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass