from rest_framework import serializers

from restapi.etl.models.silver import PatientDim, SurveyFact

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

class MainFactSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyFact
        fields = [
            "surveying_organization",
            "surveying_user",
            "community",
            "question",
            "question_answer",
            "created_at",
            "updated_at",
            "form",
            "patient",
            "household_id"
        ]