# Description

It provides a smart status bar for loops. It can be used to display the progress of a long running operation

# Usage

##	status_bar(index, total, message)

	index : current iteration of our loop
	total : total number of iteration of out loop
	message : Unique message for each iteration

# Example

	import smart_status_bar 
	import time

	LOOP = 50
	for i in range(LOOP):
		smart_status_bar.status_bar(i, LOOP, f"This is iteration {i}")
		time.sleep(0.2)