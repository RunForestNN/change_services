import os

from testJob.settings import INSTALLED_APPS
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testJob.settings")

app = Celery("testJob")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.broker_connection_retry_on_startup = True
app.autodiscover_tasks(lambda: INSTALLED_APPS)
