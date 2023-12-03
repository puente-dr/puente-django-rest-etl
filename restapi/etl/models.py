# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


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
    household = models.ForeignKey(HouseholdDim, models.DO_NOTHING)

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
    question_answer = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    form = models.ForeignKey(FormDim, models.DO_NOTHING)
    patient = models.ForeignKey(PatientDim, models.DO_NOTHING)
    household = models.ForeignKey(HouseholdDim, models.DO_NOTHING)

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
    user_name = models.CharField(max_length=255)
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
