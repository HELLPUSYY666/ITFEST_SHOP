from django.apps import AppConfig


class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Fisrt'

    def ready(self):
        import ITFest.Fisrt.signals
