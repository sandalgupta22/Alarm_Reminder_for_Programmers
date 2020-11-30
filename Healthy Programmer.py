
from time import time
from datetime import datetime
from pygame import mixer

def water():
    mixer.init()
    mixer.music.load("D:\\water.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play(loops=25)

def stop():
    mixer.music.stop()

def eyes():
    mixer.init()
    mixer.music.load("D:\\eyes.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play(loops=25)

def physical():
    mixer.init()
    mixer.music.load("D:\\physical.mp3")
    mixer.music.set_volume(0.1)
    mixer.music.play(loops=25)

def water_log():
    f = open("water plan", "a")
    f.write("Water drank at : \t")
    f.write(str(datetime.now()))
    f.write("\n")

def eyes_log():
    f = open("eyes excersise plan", "a")
    f.write("Eyes Excersise done at : \t")
    f.write(str(datetime.now()))
    f.write("\n")

def phy_log():
    f = open("physical excersise plan", "a")
    f.write("Physical Excersise done at : \t")
    f.write(str(datetime.now()))
    f.write("\n")

if __name__ == '__main__':
    init_water=time()
    init_eyes=time()
    init_phy=time()
    watersec=2400
    eyesec=1800
    physec=2700

    while True:
        if (time()-init_water>watersec):

            print("\nPlease Drink 350 ml water its been a long since you last drank water ")
            water()
            init_water=time()
            print("\n Enter 'drank' to stop the alarm \n")

            while(True):
                a = input("Status : ")
                if (a=="drank") or (a=="Drank") or (a=="DRANK"):
                    water_log()
                    stop()
                    break
                else:
                    continue

        if(time()-init_eyes>eyesec):
            print("\nIts time for your Eye Excersise its been half hour looking straight at computer screen  \n")
            eyes()
            init_eyes=time()
            print("Enter 'eydone' to stop the alarm\n")
            while(True):
                b=input("Status : ")
                if (b=="eydone") or (b=="EyDone") or (b=="EYDONE") or (b=="eyDone") or (b=="Eydone"):
                    eyes_log()
                    stop()
                    break
                else:
                    continue

        if (time()-init_phy>physec):

            print("\nIts Time for some Physical Activity its been 45 min you are continuously sitting infront of desktop ")
            physical()
            init_phy=time()
            print("\nEnter 'exdone' to stop the alarm \n")
            while(True):
                c=input("Status : ")
                if (c=="ExDone") or (c=="exdone") or (c=="exDone") or (c=="Exdone") or (c=="EXDONE"):
                    phy_log()
                    stop()
                    break
                else:
                    continue
