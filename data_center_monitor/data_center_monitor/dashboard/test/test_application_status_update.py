import os
from unittest import TestCase
import pandas as pandas

from data_center_monitor.data_center_monitor.dashboard.application_status_update import \
	ApplicationStatusUpdate

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestApplicationStatusUpdate(TestCase):

	def setUp(self):
		self.analytic_mock_filename = os.path.join(BASE_DIR, 'test/applications_analytics_mock.csv')
		self.application_status_update = ApplicationStatusUpdate()

	def test_load_application_status_file_from_filename(self):
		self.application_status_update.load_status_file(self.analytic_mock_filename)
		self.assertIsInstance(self.application_status_update.status_analytics, pandas.DataFrame)
		assert False, self.application_status_update.status_analytics