from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'tp_subject'
    verbose_name = 'Ambition Subject CRFs'
    admin_site_name = None  # edit after creating admin site
