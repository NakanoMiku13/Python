import pywhatkit
from pynput.keyboard import Key, Controller
import time
try:
    #pywhatkit.sendwhatmsg_instantly("+525561232707","Hola mundo",0)
    keyboard = Controller()
    #key = ["S","o","f","i"," ","q","u","i","e","r","e"," ","q","u","e"," ","m","e"," ","s","a","l","g","a"]
    key = "Ya valio madres este pedo Sofi :3 <3"
    time.sleep(10)    
    while(1):
        for x in key:
            keyboard.press(x)
        keyboard.press(Key.enter)    
        keyboard.release(Key.enter)
        time.sleep(0.15)
    print("Ready")

except:
    print("Error")

