#salam
#elham ghahremani tamrin9-1
import subprocess as sub
while True:
    command=input("shell =>")
    cmd=sub.check_output(command,shell=True).decode()
    print(cmd)
    
