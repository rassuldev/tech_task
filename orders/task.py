from celery import task
# import requests
from django.conf import settings

@task.periodic_task()
def parse_google_doc():
     pass

