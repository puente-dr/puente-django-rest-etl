from django.db import models

class EvaluationmedicalBronze(models.Model):
    objectid = models.TextField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    chronic_condition_hypertension = models.TextField(blank=True, null=True)
    chronic_condition_diabetes = models.TextField(blank=True, null=True)
    chronic_condition_other = models.TextField(blank=True, null=True)
    seen_doctor = models.TextField(blank=True, null=True)
    received_treatment_description = models.TextField(blank=True, null=True)
    part_of_body = models.TextField(blank=True, null=True)
    duration = models.TextField(blank=True, null=True)
    trauma_induced = models.TextField(blank=True, null=True)
    condition_progression = models.TextField(blank=True, null=True)
    assessmentandevaluation = models.TextField(db_column='AssessmentandEvaluation', blank=True, null=True)  # Field name made lowercase.
    assessmentandevaluation_surgical = models.TextField(db_column='AssessmentandEvaluation_Surgical', blank=True, null=True)  # Field name made lowercase.
    planofaction = models.TextField(db_column='planOfAction', blank=True, null=True)  # Field name made lowercase.
    surveyinguser = models.TextField(db_column='surveyingUser', blank=True, null=True)  # Field name made lowercase.
    surveyingorganization = models.TextField(db_column='surveyingOrganization', blank=True, null=True)  # Field name made lowercase.
    appversion = models.TextField(db_column='appVersion', blank=True, null=True)  # Field name made lowercase.
    phoneos = models.TextField(db_column='phoneOS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.TextField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.TextField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    client_type = models.TextField(db_column='client.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    client_classname = models.TextField(db_column='client.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    client_objectid = models.TextField(db_column='client.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    received_treatment_notes = models.TextField(blank=True, null=True)
    immediate_follow_up = models.TextField(blank=True, null=True)
    part_of_body_description = models.TextField(blank=True, null=True)
    assessmentandevaluation_surgical_guess = models.TextField(db_column='AssessmentandEvaluation_Surgical_Guess', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(blank=True, null=True)
    parseparentclassobjectidoffline = models.TextField(db_column='parseParentClassObjectIdOffline', blank=True, null=True)  # Field name made lowercase.
    parseuser_type = models.TextField(db_column='parseUser.__type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    parseuser_classname = models.TextField(db_column='parseUser.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parseuser_objectid = models.TextField(db_column='parseUser.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pain = models.FloatField(blank=True, null=True)
    needsassessmentandevaluation = models.TextField(db_column='needsAssessmentandEvaluation', blank=True, null=True)  # Field name made lowercase.
    location_type = models.TextField(db_column='location.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    location_latitude = models.FloatField(db_column='location.latitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_longitude = models.FloatField(db_column='location.longitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    abnormal_bleeding = models.TextField(blank=True, null=True)
    difficulty_breathing = models.TextField(blank=True, null=True)
    mental_issues = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    suggested_treatment = models.FloatField(blank=True, null=True)
    received_treatment = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluationmedical_bronze'

class FormresultsBronze(models.Model):
    objectid = models.TextField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    fields = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    formspecificationsid = models.TextField(db_column='formSpecificationsId', blank=True, null=True)  # Field name made lowercase.
    surveyinguser = models.TextField(db_column='surveyingUser', blank=True, null=True)  # Field name made lowercase.
    surveyingorganization = models.TextField(db_column='surveyingOrganization', blank=True, null=True)  # Field name made lowercase.
    createdat = models.TextField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.TextField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    client_type = models.TextField(db_column='client.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    client_classname = models.TextField(db_column='client.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    client_objectid = models.TextField(db_column='client.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    appversion = models.TextField(db_column='appVersion', blank=True, null=True)  # Field name made lowercase.
    phoneos = models.TextField(db_column='phoneOS', blank=True, null=True)  # Field name made lowercase.
    parseparentclassobjectidoffline = models.TextField(db_column='parseParentClassObjectIdOffline', blank=True, null=True)  # Field name made lowercase.
    loopclient_type = models.TextField(db_column='loopClient.__type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    loopclient_classname = models.TextField(db_column='loopClient.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    loopclient_objectid = models.TextField(db_column='loopClient.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parseuser_type = models.TextField(db_column='parseUser.__type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    parseuser_classname = models.TextField(db_column='parseUser.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parseuser_objectid = models.TextField(db_column='parseUser.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    organizations = models.TextField(blank=True, null=True)
    location_type = models.TextField(db_column='location.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    location_latitude = models.FloatField(db_column='location.latitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_longitude = models.FloatField(db_column='location.longitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'formresults_bronze'

class Formspecificationsv2Bronze(models.Model):
    objectid = models.TextField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    fields = models.TextField(blank=True, null=True)
    organizations = models.TextField(blank=True, null=True)
    typeofform = models.TextField(db_column='typeOfForm', blank=True, null=True)  # Field name made lowercase.
    workflows = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    description = models.TextField(blank=True, null=True)
    customform = models.BooleanField(db_column='customForm', blank=True, null=True)  # Field name made lowercase.
    createdat = models.TextField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.TextField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    active = models.TextField(blank=True, null=True)
    location_type = models.TextField(db_column='location.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    location_latitude = models.FloatField(db_column='location.latitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_longitude = models.FloatField(db_column='location.longitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'formspecificationsv2_bronze'

class HistoryenvironmentalhealthBronze(models.Model):
    objectid = models.TextField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    biggestproblemofcommunity_v2 = models.TextField(blank=True, null=True)
    bathroomaccess_v2 = models.TextField(db_column='bathroomAccess_v2', blank=True, null=True)  # Field name made lowercase.
    clinicaccess_v2 = models.TextField(db_column='clinicAccess_v2', blank=True, null=True)  # Field name made lowercase.
    floormaterial = models.TextField(db_column='floorMaterial', blank=True, null=True)  # Field name made lowercase.
    numberofchildrenlivinginhouseundertheageof5_v2 = models.TextField(db_column='numberofChildrenLivinginHouseUndertheAgeof5_v2', blank=True, null=True)  # Field name made lowercase.
    yearslivedinthecommunity = models.TextField(db_column='yearsLivedinthecommunity', blank=True, null=True)  # Field name made lowercase.
    yearslivedinthishouse = models.TextField(db_column='yearsLivedinThisHouse', blank=True, null=True)  # Field name made lowercase.
    wateraccess = models.TextField(db_column='waterAccess', blank=True, null=True)  # Field name made lowercase.
    typeofwaterdoyoudrink = models.TextField(db_column='typeofWaterdoyoudrink', blank=True, null=True)  # Field name made lowercase.
    latrineaccess = models.TextField(db_column='latrineAccess', blank=True, null=True)  # Field name made lowercase.
    dentalaccess = models.TextField(db_column='dentalAccess', blank=True, null=True)  # Field name made lowercase.
    timesperweektrashcollected = models.TextField(blank=True, null=True)
    houseownership = models.TextField(blank=True, null=True)
    conditionofloorinyourhouse = models.TextField(db_column='conditionoFloorinyourhouse', blank=True, null=True)  # Field name made lowercase.
    conditionoroofinyourhouse = models.TextField(db_column='conditionoRoofinyourhouse', blank=True, null=True)  # Field name made lowercase.
    stovetype = models.TextField(db_column='stoveType', blank=True, null=True)  # Field name made lowercase.
    housematerial = models.TextField(db_column='houseMaterial', blank=True, null=True)  # Field name made lowercase.
    electricityaccess = models.TextField(db_column='electricityAccess', blank=True, null=True)  # Field name made lowercase.
    foodsecurity = models.TextField(db_column='foodSecurity', blank=True, null=True)  # Field name made lowercase.
    govassistance = models.TextField(db_column='govAssistance', blank=True, null=True)  # Field name made lowercase.
    numberofindividualslivinginthehouse = models.TextField(db_column='numberofIndividualsLivingintheHouse', blank=True, null=True)  # Field name made lowercase.
    surveyinguser = models.TextField(db_column='surveyingUser', blank=True, null=True)  # Field name made lowercase.
    surveyingorganization = models.TextField(db_column='surveyingOrganization', blank=True, null=True)  # Field name made lowercase.
    appversion = models.TextField(db_column='appVersion', blank=True, null=True)  # Field name made lowercase.
    phoneos = models.TextField(db_column='phoneOS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.TextField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.TextField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    client_type = models.TextField(db_column='client.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    client_classname = models.TextField(db_column='client.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    client_objectid = models.TextField(db_column='client.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parseparentclassobjectidoffline = models.TextField(db_column='parseParentClassObjectIdOffline', blank=True, null=True)  # Field name made lowercase.
    biggestproblemofcommunity = models.TextField(blank=True, null=True)
    bathroomaccess = models.TextField(db_column='bathroomAccess', blank=True, null=True)  # Field name made lowercase.
    clinicaccess = models.TextField(db_column='clinicAccess', blank=True, null=True)  # Field name made lowercase.
    numberofchildrenlivinginhouseundertheageof5 = models.TextField(db_column='numberofChildrenLivinginHouseUndertheAgeof5', blank=True, null=True)  # Field name made lowercase.
    parseuser_type = models.TextField(db_column='parseUser.__type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    parseuser_classname = models.TextField(db_column='parseUser.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parseuser_objectid = models.TextField(db_column='parseUser.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    medicalproblemswheredoyougo = models.TextField(blank=True, null=True)
    dentalproblemswheredoyougo = models.TextField(blank=True, null=True)
    wheretrashleftbetweenpickups = models.TextField(blank=True, null=True)
    location_type = models.TextField(db_column='location.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    location_latitude = models.FloatField(db_column='location.latitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_longitude = models.FloatField(db_column='location.longitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'historyenvironmentalhealth_bronze'

class SurveydataBronze(models.Model):
    objectid = models.TextField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    searchindex = models.TextField(db_column='searchIndex', blank=True, null=True)  # Field name made lowercase.
    fname = models.TextField(blank=True, null=True)
    lname = models.TextField(blank=True, null=True)
    sex = models.TextField(blank=True, null=True)
    marriagestatus = models.TextField(db_column='marriageStatus', blank=True, null=True)  # Field name made lowercase.
    educationlevel = models.TextField(db_column='educationLevel', blank=True, null=True)  # Field name made lowercase.
    communityname = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    province = models.TextField(blank=True, null=True)
    surveyingorganization = models.TextField(db_column='surveyingOrganization', blank=True, null=True)  # Field name made lowercase.
    surveyinguser = models.TextField(db_column='surveyingUser', blank=True, null=True)  # Field name made lowercase.
    appversion = models.TextField(db_column='appVersion', blank=True, null=True)  # Field name made lowercase.
    phoneos = models.TextField(db_column='phoneOS', blank=True, null=True)  # Field name made lowercase.
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    dob = models.TextField(blank=True, null=True)
    fulltextsearchindex = models.TextField(db_column='fullTextSearchIndex', blank=True, null=True)  # Field name made lowercase.
    createdat = models.TextField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.TextField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    occupation = models.TextField(blank=True, null=True)
    nickname = models.TextField(blank=True, null=True)
    telephonenumber = models.TextField(db_column='telephoneNumber', blank=True, null=True)  # Field name made lowercase.
    region = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    location_type = models.TextField(db_column='location.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    location_latitude = models.FloatField(db_column='location.latitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_longitude = models.FloatField(db_column='location.longitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    age = models.TextField(blank=True, null=True)
    objectidoffline = models.TextField(db_column='objectIdOffline', blank=True, null=True)  # Field name made lowercase.
    subcounty = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    householdid = models.TextField(db_column='householdId', blank=True, null=True)  # Field name made lowercase.
    householdobjectidoffline = models.TextField(db_column='householdObjectIdOffline', blank=True, null=True)  # Field name made lowercase.
    householdclient_type = models.TextField(db_column='householdClient.__type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    householdclient_classname = models.TextField(db_column='householdClient.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    householdclient_objectid = models.TextField(db_column='householdClient.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    picture_type = models.TextField(db_column='picture.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    picture_name = models.TextField(db_column='picture.name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    picture_url = models.TextField(db_column='picture.url', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    parseuser_type = models.TextField(db_column='parseUser.__type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    parseuser_classname = models.TextField(db_column='parseUser.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parseuser_objectid = models.TextField(db_column='parseUser.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    familyrelationships = models.FloatField(db_column='familyRelationships', blank=True, null=True)  # Field name made lowercase.
    insurancenumber = models.TextField(db_column='insuranceNumber', blank=True, null=True)  # Field name made lowercase.
    insuranceprovider = models.TextField(db_column='insuranceProvider', blank=True, null=True)  # Field name made lowercase.
    clinicprovider = models.TextField(db_column='clinicProvider', blank=True, null=True)  # Field name made lowercase.
    cedulanumber = models.TextField(db_column='cedulaNumber', blank=True, null=True)  # Field name made lowercase.
    signature_type = models.TextField(db_column='signature.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    signature_name = models.TextField(db_column='signature.name', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    signature_url = models.TextField(db_column='signature.url', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    relationship = models.TextField(blank=True, null=True)
    relationship_id = models.TextField(blank=True, null=True)
    numberofindividualslivinginthehouse = models.TextField(db_column='numberofIndividualsLivingintheHouse', blank=True, null=True)  # Field name made lowercase.
    numberofchildrenlivinginhouseundertheageof5 = models.TextField(db_column='numberofChildrenLivinginHouseUndertheAgeof5', blank=True, null=True)  # Field name made lowercase.
    yearslivedinthecommunity = models.TextField(db_column='yearsLivedinthecommunity', blank=True, null=True)  # Field name made lowercase.
    yearslivedinthishouse = models.TextField(db_column='yearsLivedinThisHouse', blank=True, null=True)  # Field name made lowercase.
    memberofthefollowingorganizations = models.TextField(blank=True, null=True)
    wateraccess = models.TextField(db_column='waterAccess', blank=True, null=True)  # Field name made lowercase.
    trashdisposallocation = models.TextField(db_column='trashDisposalLocation', blank=True, null=True)  # Field name made lowercase.
    familyhistory = models.TextField(blank=True, null=True)
    otherorganizationsyouknow = models.TextField(db_column='otherOrganizationsYouKnow', blank=True, null=True)  # Field name made lowercase.
    numberofchildrenlivinginthehouse = models.FloatField(db_column='numberofChildrenLivingintheHouse', blank=True, null=True)  # Field name made lowercase.
    daymostconvenient = models.FloatField(db_column='dayMostConvenient', blank=True, null=True)  # Field name made lowercase.
    hourmostconvenient = models.FloatField(db_column='hourMostConvenient', blank=True, null=True)  # Field name made lowercase.
    medicalillnesses2 = models.FloatField(db_column='medicalIllnesses2', blank=True, null=True)  # Field name made lowercase.
    whendiagnosed2 = models.FloatField(db_column='whenDiagnosed2', blank=True, null=True)  # Field name made lowercase.
    whatdoctordoyousee2 = models.FloatField(db_column='whatDoctorDoyousee2', blank=True, null=True)  # Field name made lowercase.
    diddoctorrecommend2 = models.FloatField(db_column='didDoctorRecommend2', blank=True, null=True)  # Field name made lowercase.
    treatment2 = models.FloatField(blank=True, null=True)
    dentalassessmentandevaluation = models.FloatField(db_column='DentalAssessmentandEvaluation', blank=True, null=True)  # Field name made lowercase.
    picture = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surveydata_bronze'

class UsersBronze(models.Model):
    objectid = models.TextField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(blank=True, null=True)
    lastname = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)
    phonenumber = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    adminverified = models.BooleanField(db_column='adminVerified', blank=True, null=True)  # Field name made lowercase.
    emailverified = models.BooleanField(db_column='emailVerified', blank=True, null=True)  # Field name made lowercase.
    createdat = models.TextField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.TextField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_bronze'

class VitalsBronze(models.Model):
    objectid = models.TextField(db_column='objectId', blank=True, null=True)  # Field name made lowercase.
    bloodsugar = models.TextField(db_column='bloodSugar', blank=True, null=True)  # Field name made lowercase.
    surveyinguser = models.TextField(db_column='surveyingUser', blank=True, null=True)  # Field name made lowercase.
    surveyingorganization = models.TextField(db_column='surveyingOrganization', blank=True, null=True)  # Field name made lowercase.
    appversion = models.TextField(db_column='appVersion', blank=True, null=True)  # Field name made lowercase.
    phoneos = models.TextField(db_column='phoneOS', blank=True, null=True)  # Field name made lowercase.
    bloodpressure = models.TextField(db_column='bloodPressure', blank=True, null=True)  # Field name made lowercase.
    createdat = models.TextField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updatedat = models.TextField(db_column='updatedAt', blank=True, null=True)  # Field name made lowercase.
    client_type = models.TextField(db_column='client.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    client_classname = models.TextField(db_column='client.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    client_objectid = models.TextField(db_column='client.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    height = models.TextField(blank=True, null=True)
    weight = models.TextField(blank=True, null=True)
    temp = models.TextField(blank=True, null=True)
    pulse = models.TextField(blank=True, null=True)
    hemoglobina1c = models.TextField(db_column='hemoglobinA1c', blank=True, null=True)  # Field name made lowercase.
    bloodoxygen = models.TextField(db_column='bloodOxygen', blank=True, null=True)  # Field name made lowercase.
    hemoglobinlevels = models.TextField(db_column='hemoglobinLevels', blank=True, null=True)  # Field name made lowercase.
    resprate = models.TextField(db_column='respRate', blank=True, null=True)  # Field name made lowercase.
    bmi = models.TextField(blank=True, null=True)
    painlevels = models.TextField(db_column='painLevels', blank=True, null=True)  # Field name made lowercase.
    parseuser_type = models.TextField(db_column='parseUser.__type', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    parseuser_classname = models.TextField(db_column='parseUser.className', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    parseuser_objectid = models.TextField(db_column='parseUser.objectId', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    location_type = models.TextField(db_column='location.__type', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it contained more than one '_' in a row.
    location_latitude = models.FloatField(db_column='location.latitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    location_longitude = models.FloatField(db_column='location.longitude', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'vitals_bronze'
