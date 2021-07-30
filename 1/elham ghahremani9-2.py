#salam
#elham ghahremani tamrin9-2
import subprocess as sub
while True:
    ip=input("enter IP:")
    cmd=sub.check_output("ping -n 10 "+ip,shell=True).decode()
    print(cmd)
    print()
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print()
      
