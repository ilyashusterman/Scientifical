from django.views.generic import TemplateView
from django.shortcuts import render

from data_center_monitor.dashboard.statistic_dashboard import \
	StatisticDashboard


class StatisticsView(TemplateView):
	template_name = "statistics.html"

	def get(self, request, *args, **kwargs):
		statistics_dashboard = StatisticDashboard()
		return render(request, self.template_name, {'statistics_dashboard': statistics_dashboard})