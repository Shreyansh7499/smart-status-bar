#!/usr/bin/python3

import time
from .colors import colors

time_start = None

	
def progress(index, total):
	bar = '|' + colors.bg.green
	for i in range (100):
		if (index / (total)) > (i / 100) :
			bar += ' '
		elif bar.find(colors.reset) == -1:
			bar += colors.reset
		else:
			bar += ' '
	bar += colors.reset + colors.fg.green + '|' + colors.reset + colors.bold
	return bar, round((index / (total))*100, 2)


def get_time_str(time):
	if (time < 60):
		return str(round(time, 2)) + 's' 
	time /= 60
	if (time < 60):
		return str(round(time, 2)) + 'm' 
	time /= 60
	if (time < 60):
		return str(round(time, 2)) + 'h'


def get_times(percentage):
	global time_start
	curr_time = time.time() - time_start

	try:
		eta = get_time_str(((curr_time * 100) / percentage) - curr_time)
	except Exception:
		eta = "inf"
	finally:
		return get_time_str(curr_time), eta


def status_bar(index, total, message = ''):
	global time_start

	if time_start == None:
		time_start = time.time()

	if index == total - 1:
		end = '\n'
	else:
		end = '\r'

	progress_bar, percentage = progress(index, total)
	curr_time, eta = get_times(percentage)

	print(f"{colors.bold}{colors.fg.lightcyan}Status: {colors.fg.purple}Time: {colors.fg.lightblue}{curr_time} {colors.fg.purple}ETA: {colors.fg.lightblue}{eta} {colors.fg.green}{progress_bar} {colors.fg.red}{percentage} % Done. {colors.fg.yellow}{message}{colors.reset}", end=end, flush=True)
