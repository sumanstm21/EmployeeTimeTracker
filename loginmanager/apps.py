from django.apps import AppConfig


class LoginmanagerConfig(AppConfig):
    name = 'loginmanager'

    def ready(self):
        import loginmanager.signals
