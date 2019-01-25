import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','data_center_monitor.settings')
django.setup()


if __name__ == '__main__':
	from data_center_monitor.dashboard.application_status_update import \
		ApplicationStatusUpdate

	ApplicationStatusUpdate().run()