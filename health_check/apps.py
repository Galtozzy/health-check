# -*- coding: utf-8 -*-
"""Django application config module.
"""
from django.apps import AppConfig

from health_check.settings import settings


class HealthCheck(AppConfig):
    name = 'health_check'
    verbose_name = 'Health Check'

    def ready(self):
        settings.build_from_django()
