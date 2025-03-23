from django.apps import AppConfig
from decouple import config

iface = config("INTERFACE_NAME", default="Wi-Fi")

class MonitorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitor'


    def ready(self):
        from .sniffer import start_sniffer
        start_sniffer(iface=iface)

