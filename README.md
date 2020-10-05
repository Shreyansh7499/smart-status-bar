# Description

It provides a smart status bar for loops. It can be used to display the progress of a long running operation

# Install

	pip3 install smart-status-bar-shreyansh7499 

# Usage
	loop:
	    """loop statements"""
	    smart_status_bar.status_bar(index, total, message)

	where
	    index : current iteration of our loop
	    total : total number of iteration of out loop
	    message : Unique message for each iteration

# Example
<pre><code>
import smart_status_bar 
import time

LOOP = 50
for i in range(LOOP):
	smart_status_bar.status_bar(i, LOOP, f"This is iteration {i}")
	time.sleep(0.2)
</code></pre>

![Alt text](https://github.com/Shreyansh7499/smart-status-bar/blob/main/Screenshots/Screenshot_1.png?raw=true "Example 1")
<br>
![Alt text](https://github.com/Shreyansh7499/smart-status-bar/blob/main/Screenshots/Screenshot_2.png?raw=true "Example 1")
