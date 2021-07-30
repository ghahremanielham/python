#salam
#elham ghahremani tamrin9-4
import subprocess as sub



sys_div=[]
div=["A:","B:","C:","D:","E:","F:","G:","H:","I:","Z:","N:"]
cmd_1 = sub.check_output("net share",shell=True).decode()
for x in div:
    if x in str(cmd_1):
        sys_div.append(x)

        
File=input("enter file name : ")

for i in sys_div:
    try:
        cmd = sub.check_output("dir/ S/ B "+i+"\\"+File, shell=True).decode()
    except sub.CalledProcessError:
        pass
  
print(cmd)
