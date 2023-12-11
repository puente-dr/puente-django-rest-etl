from rest_framework import serializers

from restapi.etl.models.bronze import HistoryenvironmentalhealthBronze

class HistoryenvironmentalhealthBronzeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistoryenvironmentalhealthBronze
        fields = [
            "biggestproblemofcommunity_v2",
            "bathroomaccess_v2",
            "clinicaccess_v2",
            "floormaterial",
            "numberofchildrenlivinginhouseundertheageof5_v2",
            "yearslivedinthecommunity",
            "yearslivedinthishouse",
            "wateraccess",
            "typeofwaterdoyoudrink",
            "latrineaccess",
            "dentalaccess",
            "timesperweektrashcollected",
            "houseownership",
            "conditionofloorinyourhouse",
            "conditionoroofinyourhouse",
            "stovetype",
            "housematerial",
            "electricityaccess",
            "foodsecurity",
            "govassistance",
            "numberofindividualslivinginthehouse",
            "surveyinguser",
            "surveyingorganization",
            "createdat",
            "updatedat",
            "biggestproblemofcommunity",
            "bathroomaccess",
            "clinicaccess",
            "numberofchildrenlivinginhouseundertheageof5",
            "medicalproblemswheredoyougo",
            "dentalproblemswheredoyougo",
            "wheretrashleftbetweenpickups",
            "location_latitude",
            "location_longitude"
        ]