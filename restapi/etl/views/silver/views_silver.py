from django.db.models import Count

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from restapi.etl.models.silver import PatientDim, SurveyFact

from restapi.etl.serializers.silver import PatientDimSerializer, MainFactSerializer

from operator import itemgetter


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

    def list_filter_sort(self, request):
        # Get parameters for sorting and filtering
        sort_by = request.query_params.get('sort_by', None)
        order = request.query_params.get('order', 'asc')  # default ascending order
        filter_criteria = request.query_params.get('filter_criteria', None)

        # Apply filtering if criteria is provided
        queryset = self.queryset
        if filter_criteria:
            queryset = queryset.filter(**filter_criteria)

        # Apply sorting if sort_by parameter is provided
        if sort_by:
            if order == 'asc':
                queryset = queryset.order_by(sort_by)
            elif order == 'desc':
                queryset = queryset.order_by('-' + sort_by)

        # Serialize the queryset and return response
        serializer = PatientDimSerializer(queryset, many=True)
        return Response(serializer.data)



    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass

class FactViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving raw Environmental Health records
    """
    queryset = SurveyFact.objects.all()

    def list(self, request):
        serializer = MainFactSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        patient_record = get_object_or_404(self.queryset, pk=pk)
        serializer = MainFactSerializer(patient_record)
        return Response(serializer)
    
    @action(detail=False, methods=['post'])
    def get_count(self, request, pk=None):
        fields = request.data.get('fields', [])
        field = fields[0]
        queryset = SurveyFact.objects.values(field).annotate(count_of_unique_values=Count('*')).order_by("-count_of_unique_values")
        return Response(queryset)

    @action(detail=False, methods=['post'])
    def list_filter_sort(self, request):
        # Get parameters for sorting and filtering if you're using query paramters
        # sort_by = request.query_params.get('sort_by', None)
        # order = request.query_params.get('order', 'asc')  # default ascending order
        # filter_criteria = request.query_params.get('filter_criteria', None)

        parameters = request.data.get('parameters')
        
        filter_criteria, sort_by, order = itemgetter('filter_criteria', 'sort_by', 'order')(parameters)

        # Apply filtering if criteria is provided
        queryset = SurveyFact.objects.select_related('patient')
    
        if filter_criteria:
            queryset = queryset.filter(**filter_criteria)

        # # Apply sorting if sort_by parameter is provided
        if sort_by:
            if order == 'asc':
                queryset = queryset.order_by(sort_by)
            elif order == 'desc':
                queryset = queryset.order_by('-' + sort_by)

        # Serialize the queryset and return response
        serializer = MainFactSerializer(queryset, many=True)
        return Response(serializer.data)