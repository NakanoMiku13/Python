#importing pynput lib to make this work
from pynput.keyboard import Key, Controller
#import time lib to set pauses
import time
try:
	#in my case i put a pause here (some problems in my terminal and do not start well and need to wait a second
	#in your case maybe this would be not necesary
	time.sleep(1)
	keyboard=Controller()
	#setting the admin password, this is a test one, so here you have to write yours
	pwd="141601"
	#setting the full command, in this case is linked to my folders, you only have to change for yours
	#the syntax is this
	#sudo rsync -ah --progress /your/directory/ /your/destinyFolder...
	#I concat the other commands to use a single line
	key1="sudo rsync -ah --progress /home/miku/Documents/ /media/usb/Backup && sudo rsync -ah --progress /home/miku/Downloads /media/usb/Backup && sudo rsync -ah --progress /home/miku/Desktop /media/usb/Backup  && sudo rsync -ah --progress /home/miku/Videos /media/usb/Backup  && sudo rsync -ah --progress /home/miku/Codigos /media/usb/Backup && sudo rsync -ah --progress /home/miku/Pictures /media/usb/Backup"
	#The final command to close the command prompt after the process finished
	key2="exit"
	#Here is invoked the command prompt
	keyboard.press(Key.ctrl)
	keyboard.press(Key.shift)
	keyboard.press('t')
	keyboard.release(Key.ctrl)
	keyboard.release(Key.shift)
	keyboard.release('t')
	#A pause
	time.sleep(1)
	#The program type all the command line into the command prompt
	for x in key1:
		keyboard.press(x)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	#Here this type your password, remember that this is optional, I set this for ez use
	for x in pwd:
		keyboard.press(x)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	#Here when the copy process is finished the command prompt it's closed
	for x in key2:
		keyboard.press(x)
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
except:
  print("Error")

