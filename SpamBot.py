from pynput.keyboard import Key, Controller
import time
try:
  keyboard=Controller()
  key="#Coinary"
  time.sleep(10)
  while(1):
       for x in key:
        	keyboard.press(x)
       keyboard.press(Key.enter)
       keyboard.release(Key.enter)
       time.sleep(0.12)
  print("Ready")
except:
  print("Error")
