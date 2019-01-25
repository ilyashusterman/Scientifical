import os
import pandas

from data_center_monitor.models import ApplicationProcess
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ANALYTICS_FILENAME = os.path.join(BASE_DIR, 'applications_analytics.csv')


class ApplicationStatusUpdate(object):

	def __init__(self):
		self.status_analytics = None

	def load_status_file(self, filename=None):
		filename = ANALYTICS_FILENAME if filename is None else filename
		self.status_analytics = pandas.read_csv(filename)

	def update_db(self):
		for application_process in self.status_analytics.itertuples():
			ApplicationProcess.objects.create(name=application_process.name,
			                                  pid=application_process.pid,
			                                  cpu_frequency=application_process.cpu_frequency,
			                                  voltage=application_process.voltage,
			                                  temperature=application_process.temperature,
			                                  num_threads=application_process.num_threads,
			                                  memory_consumption=application_process.memory_consumption)

	def run(self, filename=None):
		self.load_status_file(filename)
		self.update_db()