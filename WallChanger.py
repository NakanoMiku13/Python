import os
import random
import time
images = os.listdir("/home/miku/Pictures/Anime/")
print(images)
configs = list()
while(True):
    file = open("/home/miku/.config/xfce4/terminal/terminalrc","r+").readlines()
    settings = dict()
    for setting in file:
        try:
            config = setting.strip().split("=",1)
            if(len(config) > 1):
                settings[config[0]] = config[1]
        except Exception as ex:
            print(ex)
    ran = random.randint(0,len(images))
    for key in settings.keys():
        if(key=="BackgroundImageFile"):
            settings[key] = settings[key].replace(settings[key],"/home/miku/Pictures/Anime/"+images[ran])
    file = open("/home/miku/.config/xfce4/terminal/terminalrc","w")
    file.write("[Configuration]\n")
    for key in settings.keys():
        file.write(str(key+"="+settings[key])+"\n")
    file.close()
    time.sleep(5)
