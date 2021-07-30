import paramiko
import time
from paramiko import SSHClient

File = open ("Roter.txt")
List = list (File)
USERNAME = List[1]
PASSWORD = List[2]
ENABLE_PASS = List[3]

for line in File.readlines():
    HOST = line.strip()
    SSH = paramiko.SSHClient()
    SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    SSH.connect(HOST, username=USERNAME, password=PASSWORD)
    Console = SSH.invoke_shell()
    Console.recv(65535)
    Console.send("en\n".encode())
    time.sleep(1)
    Console.send(ENABLE_PASS.encode() + "\n".encode())
    time.sleep(1)
    Console.send("conf t\n".encode())
    elnet.write("snmp-server community pub1 rw\n".encode())
    time.sleep(1)
    time.sleep(1)
    Console.send("hostname Ghahremani\n".encode())
    time.sleep(1)
    Console.recv(65535)
    Console.send("end\n".encode())
    time.sleep(1)
    SSH.close()
