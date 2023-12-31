# Generated by Django 4.2.7 on 2023-12-11 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CommunityDim',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'community_dim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='EvaluationmedicalBronze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.TextField(blank=True, db_column='objectId', null=True)),
                ('chronic_condition_hypertension', models.TextField(blank=True, null=True)),
                ('chronic_condition_diabetes', models.TextField(blank=True, null=True)),
                ('chronic_condition_other', models.TextField(blank=True, null=True)),
                ('seen_doctor', models.TextField(blank=True, null=True)),
                ('received_treatment_description', models.TextField(blank=True, null=True)),
                ('part_of_body', models.TextField(blank=True, null=True)),
                ('duration', models.TextField(blank=True, null=True)),
                ('trauma_induced', models.TextField(blank=True, null=True)),
                ('condition_progression', models.TextField(blank=True, null=True)),
                ('assessmentandevaluation', models.TextField(blank=True, db_column='AssessmentandEvaluation', null=True)),
                ('assessmentandevaluation_surgical', models.TextField(blank=True, db_column='AssessmentandEvaluation_Surgical', null=True)),
                ('planofaction', models.TextField(blank=True, db_column='planOfAction', null=True)),
                ('surveyinguser', models.TextField(blank=True, db_column='surveyingUser', null=True)),
                ('surveyingorganization', models.TextField(blank=True, db_column='surveyingOrganization', null=True)),
                ('appversion', models.TextField(blank=True, db_column='appVersion', null=True)),
                ('phoneos', models.TextField(blank=True, db_column='phoneOS', null=True)),
                ('createdat', models.TextField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.TextField(blank=True, db_column='updatedAt', null=True)),
                ('client_type', models.TextField(blank=True, db_column='client.__type', null=True)),
                ('client_classname', models.TextField(blank=True, db_column='client.className', null=True)),
                ('client_objectid', models.TextField(blank=True, db_column='client.objectId', null=True)),
                ('received_treatment_notes', models.TextField(blank=True, null=True)),
                ('immediate_follow_up', models.TextField(blank=True, null=True)),
                ('part_of_body_description', models.TextField(blank=True, null=True)),
                ('assessmentandevaluation_surgical_guess', models.TextField(blank=True, db_column='AssessmentandEvaluation_Surgical_Guess', null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('parseparentclassobjectidoffline', models.TextField(blank=True, db_column='parseParentClassObjectIdOffline', null=True)),
                ('parseuser_type', models.TextField(blank=True, db_column='parseUser.__type', null=True)),
                ('parseuser_classname', models.TextField(blank=True, db_column='parseUser.className', null=True)),
                ('parseuser_objectid', models.TextField(blank=True, db_column='parseUser.objectId', null=True)),
                ('pain', models.FloatField(blank=True, null=True)),
                ('needsassessmentandevaluation', models.TextField(blank=True, db_column='needsAssessmentandEvaluation', null=True)),
                ('location_type', models.TextField(blank=True, db_column='location.__type', null=True)),
                ('location_latitude', models.FloatField(blank=True, db_column='location.latitude', null=True)),
                ('location_longitude', models.FloatField(blank=True, db_column='location.longitude', null=True)),
                ('abnormal_bleeding', models.TextField(blank=True, null=True)),
                ('difficulty_breathing', models.TextField(blank=True, null=True)),
                ('mental_issues', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('diagnosis', models.TextField(blank=True, null=True)),
                ('suggested_treatment', models.FloatField(blank=True, null=True)),
                ('received_treatment', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'evaluationmedical_bronze',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormDim',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
                ('is_custom_form', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'form_dim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormresultsBronze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.TextField(blank=True, db_column='objectId', null=True)),
                ('fields', models.TextField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('formspecificationsid', models.TextField(blank=True, db_column='formSpecificationsId', null=True)),
                ('surveyinguser', models.TextField(blank=True, db_column='surveyingUser', null=True)),
                ('surveyingorganization', models.TextField(blank=True, db_column='surveyingOrganization', null=True)),
                ('createdat', models.TextField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.TextField(blank=True, db_column='updatedAt', null=True)),
                ('client_type', models.TextField(blank=True, db_column='client.__type', null=True)),
                ('client_classname', models.TextField(blank=True, db_column='client.className', null=True)),
                ('client_objectid', models.TextField(blank=True, db_column='client.objectId', null=True)),
                ('appversion', models.TextField(blank=True, db_column='appVersion', null=True)),
                ('phoneos', models.TextField(blank=True, db_column='phoneOS', null=True)),
                ('parseparentclassobjectidoffline', models.TextField(blank=True, db_column='parseParentClassObjectIdOffline', null=True)),
                ('loopclient_type', models.TextField(blank=True, db_column='loopClient.__type', null=True)),
                ('loopclient_classname', models.TextField(blank=True, db_column='loopClient.className', null=True)),
                ('loopclient_objectid', models.TextField(blank=True, db_column='loopClient.objectId', null=True)),
                ('parseuser_type', models.TextField(blank=True, db_column='parseUser.__type', null=True)),
                ('parseuser_classname', models.TextField(blank=True, db_column='parseUser.className', null=True)),
                ('parseuser_objectid', models.TextField(blank=True, db_column='parseUser.objectId', null=True)),
                ('organizations', models.TextField(blank=True, null=True)),
                ('location_type', models.TextField(blank=True, db_column='location.__type', null=True)),
                ('location_latitude', models.FloatField(blank=True, db_column='location.latitude', null=True)),
                ('location_longitude', models.FloatField(blank=True, db_column='location.longitude', null=True)),
            ],
            options={
                'db_table': 'formresults_bronze',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Formspecificationsv2Bronze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.TextField(blank=True, db_column='objectId', null=True)),
                ('fields', models.TextField(blank=True, null=True)),
                ('organizations', models.TextField(blank=True, null=True)),
                ('typeofform', models.TextField(blank=True, db_column='typeOfForm', null=True)),
                ('workflows', models.TextField(blank=True, null=True)),
                ('name', models.TextField(blank=True, null=True)),
                ('class_field', models.TextField(blank=True, db_column='class', null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('customform', models.BooleanField(blank=True, db_column='customForm', null=True)),
                ('createdat', models.TextField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.TextField(blank=True, db_column='updatedAt', null=True)),
                ('active', models.TextField(blank=True, null=True)),
                ('location_type', models.TextField(blank=True, db_column='location.__type', null=True)),
                ('location_latitude', models.FloatField(blank=True, db_column='location.latitude', null=True)),
                ('location_longitude', models.FloatField(blank=True, db_column='location.longitude', null=True)),
            ],
            options={
                'db_table': 'formspecificationsv2_bronze',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryenvironmentalhealthBronze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.TextField(blank=True, db_column='objectId', null=True)),
                ('biggestproblemofcommunity_v2', models.TextField(blank=True, null=True)),
                ('bathroomaccess_v2', models.TextField(blank=True, db_column='bathroomAccess_v2', null=True)),
                ('clinicaccess_v2', models.TextField(blank=True, db_column='clinicAccess_v2', null=True)),
                ('floormaterial', models.TextField(blank=True, db_column='floorMaterial', null=True)),
                ('numberofchildrenlivinginhouseundertheageof5_v2', models.TextField(blank=True, db_column='numberofChildrenLivinginHouseUndertheAgeof5_v2', null=True)),
                ('yearslivedinthecommunity', models.TextField(blank=True, db_column='yearsLivedinthecommunity', null=True)),
                ('yearslivedinthishouse', models.TextField(blank=True, db_column='yearsLivedinThisHouse', null=True)),
                ('wateraccess', models.TextField(blank=True, db_column='waterAccess', null=True)),
                ('typeofwaterdoyoudrink', models.TextField(blank=True, db_column='typeofWaterdoyoudrink', null=True)),
                ('latrineaccess', models.TextField(blank=True, db_column='latrineAccess', null=True)),
                ('dentalaccess', models.TextField(blank=True, db_column='dentalAccess', null=True)),
                ('timesperweektrashcollected', models.TextField(blank=True, null=True)),
                ('houseownership', models.TextField(blank=True, null=True)),
                ('conditionofloorinyourhouse', models.TextField(blank=True, db_column='conditionoFloorinyourhouse', null=True)),
                ('conditionoroofinyourhouse', models.TextField(blank=True, db_column='conditionoRoofinyourhouse', null=True)),
                ('stovetype', models.TextField(blank=True, db_column='stoveType', null=True)),
                ('housematerial', models.TextField(blank=True, db_column='houseMaterial', null=True)),
                ('electricityaccess', models.TextField(blank=True, db_column='electricityAccess', null=True)),
                ('foodsecurity', models.TextField(blank=True, db_column='foodSecurity', null=True)),
                ('govassistance', models.TextField(blank=True, db_column='govAssistance', null=True)),
                ('numberofindividualslivinginthehouse', models.TextField(blank=True, db_column='numberofIndividualsLivingintheHouse', null=True)),
                ('surveyinguser', models.TextField(blank=True, db_column='surveyingUser', null=True)),
                ('surveyingorganization', models.TextField(blank=True, db_column='surveyingOrganization', null=True)),
                ('appversion', models.TextField(blank=True, db_column='appVersion', null=True)),
                ('phoneos', models.TextField(blank=True, db_column='phoneOS', null=True)),
                ('createdat', models.TextField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.TextField(blank=True, db_column='updatedAt', null=True)),
                ('client_type', models.TextField(blank=True, db_column='client.__type', null=True)),
                ('client_classname', models.TextField(blank=True, db_column='client.className', null=True)),
                ('client_objectid', models.TextField(blank=True, db_column='client.objectId', null=True)),
                ('parseparentclassobjectidoffline', models.TextField(blank=True, db_column='parseParentClassObjectIdOffline', null=True)),
                ('biggestproblemofcommunity', models.TextField(blank=True, null=True)),
                ('bathroomaccess', models.TextField(blank=True, db_column='bathroomAccess', null=True)),
                ('clinicaccess', models.TextField(blank=True, db_column='clinicAccess', null=True)),
                ('numberofchildrenlivinginhouseundertheageof5', models.TextField(blank=True, db_column='numberofChildrenLivinginHouseUndertheAgeof5', null=True)),
                ('parseuser_type', models.TextField(blank=True, db_column='parseUser.__type', null=True)),
                ('parseuser_classname', models.TextField(blank=True, db_column='parseUser.className', null=True)),
                ('parseuser_objectid', models.TextField(blank=True, db_column='parseUser.objectId', null=True)),
                ('medicalproblemswheredoyougo', models.TextField(blank=True, null=True)),
                ('dentalproblemswheredoyougo', models.TextField(blank=True, null=True)),
                ('wheretrashleftbetweenpickups', models.TextField(blank=True, null=True)),
                ('location_type', models.TextField(blank=True, db_column='location.__type', null=True)),
                ('location_latitude', models.FloatField(blank=True, db_column='location.latitude', null=True)),
                ('location_longitude', models.FloatField(blank=True, db_column='location.longitude', null=True)),
            ],
            options={
                'db_table': 'historyenvironmentalhealth_bronze',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HouseholdDim',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'household_dim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PatientDim',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('nick_name', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('household_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'patient_dim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='QuestionDim',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=255)),
                ('field_type', models.CharField(max_length=255)),
                ('formik_key', models.CharField(blank=True, max_length=255, null=True)),
                ('options', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'question_dim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SurveydataBronze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.TextField(blank=True, db_column='objectId', null=True)),
                ('searchindex', models.TextField(blank=True, db_column='searchIndex', null=True)),
                ('fname', models.TextField(blank=True, null=True)),
                ('lname', models.TextField(blank=True, null=True)),
                ('sex', models.TextField(blank=True, null=True)),
                ('marriagestatus', models.TextField(blank=True, db_column='marriageStatus', null=True)),
                ('educationlevel', models.TextField(blank=True, db_column='educationLevel', null=True)),
                ('communityname', models.TextField(blank=True, null=True)),
                ('city', models.TextField(blank=True, null=True)),
                ('province', models.TextField(blank=True, null=True)),
                ('surveyingorganization', models.TextField(blank=True, db_column='surveyingOrganization', null=True)),
                ('surveyinguser', models.TextField(blank=True, db_column='surveyingUser', null=True)),
                ('appversion', models.TextField(blank=True, db_column='appVersion', null=True)),
                ('phoneos', models.TextField(blank=True, db_column='phoneOS', null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('altitude', models.FloatField(blank=True, null=True)),
                ('dob', models.TextField(blank=True, null=True)),
                ('fulltextsearchindex', models.TextField(blank=True, db_column='fullTextSearchIndex', null=True)),
                ('createdat', models.TextField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.TextField(blank=True, db_column='updatedAt', null=True)),
                ('occupation', models.TextField(blank=True, null=True)),
                ('nickname', models.TextField(blank=True, null=True)),
                ('telephonenumber', models.TextField(blank=True, db_column='telephoneNumber', null=True)),
                ('region', models.TextField(blank=True, null=True)),
                ('country', models.TextField(blank=True, null=True)),
                ('location_type', models.TextField(blank=True, db_column='location.__type', null=True)),
                ('location_latitude', models.FloatField(blank=True, db_column='location.latitude', null=True)),
                ('location_longitude', models.FloatField(blank=True, db_column='location.longitude', null=True)),
                ('age', models.TextField(blank=True, null=True)),
                ('objectidoffline', models.TextField(blank=True, db_column='objectIdOffline', null=True)),
                ('subcounty', models.TextField(blank=True, null=True)),
                ('other', models.TextField(blank=True, null=True)),
                ('householdid', models.TextField(blank=True, db_column='householdId', null=True)),
                ('householdobjectidoffline', models.TextField(blank=True, db_column='householdObjectIdOffline', null=True)),
                ('householdclient_type', models.TextField(blank=True, db_column='householdClient.__type', null=True)),
                ('householdclient_classname', models.TextField(blank=True, db_column='householdClient.className', null=True)),
                ('householdclient_objectid', models.TextField(blank=True, db_column='householdClient.objectId', null=True)),
                ('picture_type', models.TextField(blank=True, db_column='picture.__type', null=True)),
                ('picture_name', models.TextField(blank=True, db_column='picture.name', null=True)),
                ('picture_url', models.TextField(blank=True, db_column='picture.url', null=True)),
                ('parseuser_type', models.TextField(blank=True, db_column='parseUser.__type', null=True)),
                ('parseuser_classname', models.TextField(blank=True, db_column='parseUser.className', null=True)),
                ('parseuser_objectid', models.TextField(blank=True, db_column='parseUser.objectId', null=True)),
                ('familyrelationships', models.FloatField(blank=True, db_column='familyRelationships', null=True)),
                ('insurancenumber', models.TextField(blank=True, db_column='insuranceNumber', null=True)),
                ('insuranceprovider', models.TextField(blank=True, db_column='insuranceProvider', null=True)),
                ('clinicprovider', models.TextField(blank=True, db_column='clinicProvider', null=True)),
                ('cedulanumber', models.TextField(blank=True, db_column='cedulaNumber', null=True)),
                ('signature_type', models.TextField(blank=True, db_column='signature.__type', null=True)),
                ('signature_name', models.TextField(blank=True, db_column='signature.name', null=True)),
                ('signature_url', models.TextField(blank=True, db_column='signature.url', null=True)),
                ('relationship', models.TextField(blank=True, null=True)),
                ('relationship_id', models.TextField(blank=True, null=True)),
                ('numberofindividualslivinginthehouse', models.TextField(blank=True, db_column='numberofIndividualsLivingintheHouse', null=True)),
                ('numberofchildrenlivinginhouseundertheageof5', models.TextField(blank=True, db_column='numberofChildrenLivinginHouseUndertheAgeof5', null=True)),
                ('yearslivedinthecommunity', models.TextField(blank=True, db_column='yearsLivedinthecommunity', null=True)),
                ('yearslivedinthishouse', models.TextField(blank=True, db_column='yearsLivedinThisHouse', null=True)),
                ('memberofthefollowingorganizations', models.TextField(blank=True, null=True)),
                ('wateraccess', models.TextField(blank=True, db_column='waterAccess', null=True)),
                ('trashdisposallocation', models.TextField(blank=True, db_column='trashDisposalLocation', null=True)),
                ('familyhistory', models.TextField(blank=True, null=True)),
                ('otherorganizationsyouknow', models.TextField(blank=True, db_column='otherOrganizationsYouKnow', null=True)),
                ('numberofchildrenlivinginthehouse', models.FloatField(blank=True, db_column='numberofChildrenLivingintheHouse', null=True)),
                ('daymostconvenient', models.FloatField(blank=True, db_column='dayMostConvenient', null=True)),
                ('hourmostconvenient', models.FloatField(blank=True, db_column='hourMostConvenient', null=True)),
                ('medicalillnesses2', models.FloatField(blank=True, db_column='medicalIllnesses2', null=True)),
                ('whendiagnosed2', models.FloatField(blank=True, db_column='whenDiagnosed2', null=True)),
                ('whatdoctordoyousee2', models.FloatField(blank=True, db_column='whatDoctorDoyousee2', null=True)),
                ('diddoctorrecommend2', models.FloatField(blank=True, db_column='didDoctorRecommend2', null=True)),
                ('treatment2', models.FloatField(blank=True, null=True)),
                ('dentalassessmentandevaluation', models.FloatField(blank=True, db_column='DentalAssessmentandEvaluation', null=True)),
                ('picture', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'surveydata_bronze',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SurveyFact',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('question_answer', models.CharField(max_length=10000)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('household_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'survey_fact',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SurveyingOrganizationDim',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'surveying_organization_dim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersBronze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.TextField(blank=True, db_column='objectId', null=True)),
                ('firstname', models.TextField(blank=True, null=True)),
                ('lastname', models.TextField(blank=True, null=True)),
                ('organization', models.TextField(blank=True, null=True)),
                ('phonenumber', models.TextField(blank=True, null=True)),
                ('username', models.TextField(blank=True, null=True)),
                ('role', models.TextField(blank=True, null=True)),
                ('adminverified', models.BooleanField(blank=True, db_column='adminVerified', null=True)),
                ('emailverified', models.BooleanField(blank=True, db_column='emailVerified', null=True)),
                ('createdat', models.TextField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.TextField(blank=True, db_column='updatedAt', null=True)),
            ],
            options={
                'db_table': 'users_bronze',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersDim',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('survey_user', models.CharField(max_length=255)),
                ('user_name', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
                ('phone_number', models.CharField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'users_dim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VitalsBronze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid', models.TextField(blank=True, db_column='objectId', null=True)),
                ('bloodsugar', models.TextField(blank=True, db_column='bloodSugar', null=True)),
                ('surveyinguser', models.TextField(blank=True, db_column='surveyingUser', null=True)),
                ('surveyingorganization', models.TextField(blank=True, db_column='surveyingOrganization', null=True)),
                ('appversion', models.TextField(blank=True, db_column='appVersion', null=True)),
                ('phoneos', models.TextField(blank=True, db_column='phoneOS', null=True)),
                ('bloodpressure', models.TextField(blank=True, db_column='bloodPressure', null=True)),
                ('createdat', models.TextField(blank=True, db_column='createdAt', null=True)),
                ('updatedat', models.TextField(blank=True, db_column='updatedAt', null=True)),
                ('client_type', models.TextField(blank=True, db_column='client.__type', null=True)),
                ('client_classname', models.TextField(blank=True, db_column='client.className', null=True)),
                ('client_objectid', models.TextField(blank=True, db_column='client.objectId', null=True)),
                ('height', models.TextField(blank=True, null=True)),
                ('weight', models.TextField(blank=True, null=True)),
                ('temp', models.TextField(blank=True, null=True)),
                ('pulse', models.TextField(blank=True, null=True)),
                ('hemoglobina1c', models.TextField(blank=True, db_column='hemoglobinA1c', null=True)),
                ('bloodoxygen', models.TextField(blank=True, db_column='bloodOxygen', null=True)),
                ('hemoglobinlevels', models.TextField(blank=True, db_column='hemoglobinLevels', null=True)),
                ('resprate', models.TextField(blank=True, db_column='respRate', null=True)),
                ('bmi', models.TextField(blank=True, null=True)),
                ('painlevels', models.TextField(blank=True, db_column='painLevels', null=True)),
                ('parseuser_type', models.TextField(blank=True, db_column='parseUser.__type', null=True)),
                ('parseuser_classname', models.TextField(blank=True, db_column='parseUser.className', null=True)),
                ('parseuser_objectid', models.TextField(blank=True, db_column='parseUser.objectId', null=True)),
                ('location_type', models.TextField(blank=True, db_column='location.__type', null=True)),
                ('location_latitude', models.FloatField(blank=True, db_column='location.latitude', null=True)),
                ('location_longitude', models.FloatField(blank=True, db_column='location.longitude', null=True)),
            ],
            options={
                'db_table': 'vitals_bronze',
                'managed': False,
            },
        ),
    ]
