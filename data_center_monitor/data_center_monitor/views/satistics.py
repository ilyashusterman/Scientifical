from django.views.generic import TemplateView
from django.shortcuts import render

from data_center_monitor.models import ApplicationProcess


class StatisticsView(TemplateView):
	template_name = "statistics.html"

	def get(self, request, *args, **kwargs):
		application_processes = ApplicationProcess.objects.all()
		return render(request, self.template_name, {'statistics': {'application_processes': application_processes}})