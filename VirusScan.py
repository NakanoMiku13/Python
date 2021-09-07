#importing pynput lib to make this work
from pynput.keyboard import Key, Controller
#import time lib to set pauses
import time
try:
    #Setting the keyboard controller
    keyboard=Controller()
    pwd="141601"
    #Command to open a new Command Prompt window
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press('t')
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release('t')
    #Small pause
    time.sleep(1)
    #Main command that activates the malware detection
    str="sudo clamscan -r --bell -i /"
    #For to read and type the command on the commap prompt
    for x in str:
        keyboard.press(x)
        keyboard.release(x)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    #For to type the password
    for x in pwd:
        keyboard.press(x)
        keyboard.release(x)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
except:
  print("Error")