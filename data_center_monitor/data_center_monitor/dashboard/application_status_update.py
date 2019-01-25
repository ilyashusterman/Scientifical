import pandas

ANALYTICS_FILENAME = 'applications_analytics.csv'


class ApplicationStatusUpdate(object):

	def __init__(self):
		self.status_analytics = None

	def load_status_file(self, filename=None):
		filename = ANALYTICS_FILENAME if filename is None else filename
		self.status_analytics = pandas.read_csv(filename)