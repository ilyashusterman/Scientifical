import os
import random

import django
import pandas
os.environ.setdefault('DJANGO_SETTINGS_MODULE','data_center_monitor.settings')
django.setup()


names = ['cpu_frequency_stress', 'voltage_stress', 'temperature_stress', 'num_threads_stress', 'memory_consumption_stress']
def get_dynamic_row():
	pid = random.randint(10111, 17000)
	name = '{}_{}'.format(random.choice(names), random.randint(1, 11))
	cpu_frequency = random.randint(1000, 3900) + random.random()
	voltage = random.randint(2, 50) + random.random()
	temperature = random.randint(26, 80) + random.random()
	num_threads = random.randint(1, 6)
	memory_consumption = random.randint(1, 50) + random.random()
	return {
		'pid': pid,
       'name': name,
	    'cpu_frequency': cpu_frequency,
		       'voltage': voltage,
		       'temperature': temperature,
		       'num_threads': num_threads,
		'memory_consumption': memory_consumption
	}

def get_dynamic_df():
	rows = [get_dynamic_row() for i in range(40)]
	df = pandas.DataFrame(rows)
	return df



if __name__ == '__main__':
	from data_center_monitor.dashboard.application_status_update import \
		ApplicationStatusUpdate

	app_status_update = ApplicationStatusUpdate()
	app_status_update.status_analytics = get_dynamic_df()
	app_status_update.update_db()