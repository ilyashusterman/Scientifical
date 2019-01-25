import os

import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','data_center_monitor.settings')
django.setup()

from data_center_monitor.models import ApplicationProcess




if __name__ == '__main__':
    ApplicationProcess.objects.all().delete()