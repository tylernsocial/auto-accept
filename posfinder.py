import time
import pyautogui
import keyboard

try:
	while True:
		if keyboard.is_pressed('q'):
			print("Stopped.")
			break
		x, y = pyautogui.position()
		print(f"x: {x}, y: {y}")
		time.sleep(0.70)
except KeyboardInterrupt:
	print("Stopped.")
 