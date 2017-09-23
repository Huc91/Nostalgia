#author: Luca Ucciero
#year: 2017
#website: https://huc91.github.io/
#license: Mit License



import os
import threading
import time
from playsound import playsound


hostname = "google.com"


def is_connected():
    response = os.system("ping -c 1 " + hostname)
    print('execute is_connected')
    if response == 0:
        return True;
    else:
        return False;

#sound only if my connected to the internet, and it'a fresh connection
#to check if it's fresh.

connected = is_connected();

def modem():
    if (connected == False):
        while (connected == False):
            print("waiting for connection")
            global connected
            connected = is_connected()
            time.sleep(2)
        else:
            return True;
    #there is internet connection
    else:
        while (connected):
            print("waiting for disconnection")
            global connected
            connected = is_connected()
            time.sleep(2)
        else:
            while (connected == False):
                print("waiting for connection")
                global connected
                connected = is_connected()
                time.sleep(2)
            else:
                return True;


def playIt():
    if (modem()):
        print('To finnaly play it!!!!')
        playsound('modem.mp3')

playIt()
