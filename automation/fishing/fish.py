import pyautogui
import numpy as np
from PIL import ImageGrab
from time import sleep

# either check np.sum or if (0, 0, 0) in array

def fish():
	mx, my = pyautogui.position()

	while True:
		capture = ImageGrab.grab( bbox=(mx-10, my-10, mx+10, my+10) )
		arr = np.array(capture)
		#capture.show()

		if (0, 0, 0) not in arr:
			pyautogui.click(button='right')
			print("clicked!")
			return;

		sleep(0.005)

def run():
	sleep(5) # initial sleep

	for i in range(1000):
		pyautogui.click(button='right')
		sleep(3)
		fish()
		sleep(1)

run()