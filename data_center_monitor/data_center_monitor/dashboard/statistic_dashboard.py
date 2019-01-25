from data_center_monitor.models import ApplicationProcess


class StatisticDashboard(object):

	def __init__(self, application_processes=None):
		self.application_processes = application_processes if application_processes is not None else self.get_application_processes()

	def get_application_processes(self):
		return ApplicationProcess.objects.all()