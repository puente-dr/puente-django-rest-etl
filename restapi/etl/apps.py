from django.apps import AppConfig


class EtlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restapi.etl'
    verbose_name = "extract load and transform app"
