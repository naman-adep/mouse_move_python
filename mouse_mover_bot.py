# Import the required packages
import time
import pyautogui

# Printing an alert message to notify user the bot is running
print('NudgeBot activated, press CTRL-C to quit.')

# Moving the mouse to set distances periodically
try:
    while True:
        pyautogui.moveRel(10, 0, 0.5)
        pyautogui.moveRel(-10, 0, 0.5)
        time.sleep(10) #Moves mouse after every 10s

# Giving users a way to disable the bot 
except KeyboardInterrupt:
    print(' NudgeBot deactivated.')