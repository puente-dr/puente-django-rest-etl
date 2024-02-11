from django.db.models import Count

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from restapi.etl.models.silver import PatientDim

from restapi.etl.serializers.silver import PatientDimSerializer

"""
list /patientdimension/
create /patientdimension/new/
detail /patientdimension/1/
update /patientdimension/1/edit/
delete /patientdimension/1/delete/
any methods not dependent on an object /patientdimension/view-name/
any methods dependent on a particular object /patientdimension/1/view-name/
"""

class PatientDimensionViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving raw Environmental Health records
    """
    queryset = PatientDim.objects.all()

    def list(self, request):
        serializer = PatientDimSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        patient_record = get_object_or_404(self.queryset, pk=pk)
        serializer = PatientDimSerializer(patient_record)
        return Response(serializer)
    
    @action(detail=False, methods=['post'])
    def get_count(self, request, pk=None):
        fields = request.data.get('fields', [])
        field = fields[0]
        queryset = PatientDim.objects.values(field).annotate(count_of_unique_values=Count('*')).order_by("-count_of_unique_values")
        return Response(queryset)


    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass