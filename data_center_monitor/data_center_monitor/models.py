from django.db import models


class ApplicationProcess(models.Model):
    pid = models.IntegerField()
    name = models.CharField(max_length=50)
    cpu_frequency = models.DecimalField(decimal_places=5, max_digits=10)
    voltage = models.DecimalField(decimal_places=5, max_digits=10)
    temperature = models.DecimalField(decimal_places=5, max_digits=10)
    num_threads = models.IntegerField()
    memory_consumption = models.DecimalField(decimal_places=5, max_digits=10)
    report_time = models.DateTimeField(auto_now=True)
