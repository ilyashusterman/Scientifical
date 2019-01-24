from django.views.generic import TemplateView
from django.shortcuts import render


class StatisticsView(TemplateView):
	template_name = "statistics.html"

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {'statistics': {'test': 'test'}})