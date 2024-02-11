from rest_framework import serializers

from restapi.etl.models.silver import PatientDim

class PatientDimSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientDim
        fields = [
            "first_name",
            "last_name",
            "nick_name",
            "sex",
            "age",
            "phone_number",
            "created_at",
            "updated_at"
        ]