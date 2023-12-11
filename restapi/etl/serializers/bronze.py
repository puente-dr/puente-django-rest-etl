from rest_framework import serializers

from restapi.etl.models.bronze import HistoryenvironmentalhealthBronze

class HistoryenvironmentalhealthBronzeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistoryenvironmentalhealthBronze
        fields = [
            "biggestproblemofcommunity_v2",
            "bathroomAccess_v2",
            "clinicAccess_v2",
            "floorMaterial",
            "numberofChildrenLivinginHouseUndertheAgeof5_v2",
            "yearsLivedinthecommunity",
            "yearsLivedinThisHouse",
            "waterAccess",
            "typeofWaterdoyoudrink",
            "latrineAccess",
            "dentalAccess",
            "timesperweektrashcollected",
            "houseownership",
            "conditionoFloorinyourhouse",
            "conditionoRoofinyourhouse",
            "stoveType",
            "houseMaterial",
            "electricityAccess",
            "foodSecurity",
            "govAssistance",
            "numberofIndividualsLivingintheHouse",
            "surveyingUser",
            "surveyingOrganization",
            "biggestproblemofcommunity",
            "bathroomAccess",
            "clinicAccess",
            "numberofChildrenLivinginHouseUndertheAgeof5",
            "medicalproblemswheredoyougo",
            "dentalproblemswheredoyougo",
            "wheretrashleftbetweenpickups",
            "location_latitude",
            "location_longitude"
        ]