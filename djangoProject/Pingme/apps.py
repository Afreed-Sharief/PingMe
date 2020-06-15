from django.apps import AppConfig


class PingmeConfig(AppConfig):
    name = 'Pingme'
    def ready(self):
        import Pingme.mysignal
