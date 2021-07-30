import telnetlib
import time

File = open ("Roter.txt")
List = list (File)
USERNAME = List[1]
PASSWORD = List[2]
ENABLE_PASS = List[3]


for line in File.readlines():
    HOST = line.strip()
    telnet = telnetlib.Telnet(HOST)
    telnet.read_until("Username: ".encode())
    time.sleep(3)
    telnet.write(USERNAME.encode() + "\n".encode())
    time.sleep(3)
    telnet.read_until("Password: ".encode())
    telnet.write(PASSWORD.encode() + "\n".encode())
    time.sleep(1)
    telnet.write("en\n".encode())
    time.sleep(1)
    telnet.write(ENABLE_PASS.encode() + "\n".encode())
    time.sleep(1)
    telnet.write("conf t\n".encode())
    time.sleep(1)
    telnet.write("snmp-server community pub1 rw\n".encode())
    time.sleep(1)
    telnet.write("hostname Ghahremani\n".encode())
    time.sleep(1)
    telnet.write("end\n".encode())
    time.sleep(1)
    telnet.write("exit\n".encode())
