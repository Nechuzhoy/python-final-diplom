from django.apps import AppConfig


class ApiDrfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api_drf'
    verbose_name = 'ЛарЁк'

    def ready(self):
        """
        импортируем сигналы
        """
