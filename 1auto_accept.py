import time
import pyautogui
import keyboard

pyautogui.FAILSAFE = True

RUNNING = True
STOP_KEY = "q"
TARGET = "./assets/1accept.png"
## accept coordinates
pos_x = 957
pos_y = 714

def stop_script():
    global RUNNING
    RUNNING = False
    print("Script Stopped. Exiting...")

keyboard.add_hotkey(STOP_KEY, stop_script)

while RUNNING:
    ############ auto accept block ############
    try:
        location = pyautogui.locateOnScreen(TARGET, confidence=0.8, grayscale=True)
    except Exception as e:
        location = None

    if location is not None:
        print("i see it at", location)
        pyautogui.click(pos_x, pos_y)
        print("clicked, match accepted")
        break
    else:
        print("i dont see it")
    ############ auto accept block ############
    time.sleep(0.5)