from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    API_EXEMPT_URLS = (
        r'^api/test/$',
    )
