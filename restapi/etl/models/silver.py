from django.db import models

class CommunityDim(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'community_dim'

class FormDim(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=10000, blank=True, null=True)
    is_custom_form = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'form_dim'

class HouseholdDim(models.Model):
    uuid = models.UUIDField(primary_key=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    community = models.ForeignKey(CommunityDim, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'household_dim'

class PatientDim(models.Model):
    uuid = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    household_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_dim'

class QuestionDim(models.Model):
    uuid = models.UUIDField(primary_key=True)
    question = models.CharField(max_length=255)
    field_type = models.CharField(max_length=255)
    formik_key = models.CharField(max_length=255, blank=True, null=True)
    options = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    form = models.ForeignKey(FormDim, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'question_dim'

class SurveyFact(models.Model):
    uuid = models.UUIDField(primary_key=True)
    surveying_organization = models.ForeignKey('SurveyingOrganizationDim', models.DO_NOTHING)
    surveying_user = models.ForeignKey('UsersDim', models.DO_NOTHING)
    community = models.ForeignKey(CommunityDim, models.DO_NOTHING)
    question = models.ForeignKey(QuestionDim, models.DO_NOTHING)
    question_answer = models.CharField(max_length=10000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    form = models.ForeignKey(FormDim, models.DO_NOTHING)
    patient = models.ForeignKey(PatientDim, on_delete=models.DO_NOTHING)
    household_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_fact'

class SurveyingOrganizationDim(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'surveying_organization_dim'

class UsersDim(models.Model):
    uuid = models.UUIDField(primary_key=True)
    survey_user = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)
    surveying_organization = models.ForeignKey(SurveyingOrganizationDim, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_dim'