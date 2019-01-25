import psutil

def memory_usage():
	return dict(psutil.virtual_memory()._asdict())


def cpu_usage():
	return {'cpu_usage': '{}%'.format(psutil.cpu_percent() + 14)}


def heat_consumption():
	return {'heat': 4.2}


def voltage_consumption():
	return {'voltage': 0.2}


def is_interesting_process(name):
	processors = ['kernel', 'mdworker', 'python']
	return len([process for process in processors if process in name]) > 0


def process_ids():
	ids = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if is_interesting_process(p.info['name'])]
	return ids


if __name__ == '__main__':
	print(memory_usage())
	print(cpu_usage())
	print(heat_consumption())
	print(voltage_consumption())
	print(process_ids())