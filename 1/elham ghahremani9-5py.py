#salam
#elham ghahremani tamrin9-5
import subprocess as sub


sys_div=[]
div=["A:","B:","C:","D:","E:","F:","G:","H:","I:","Z:","N:"]
cmd_0 = sub.check_output("net share",shell=True).decode()
for x in div:
    if x in str(cmd_0):
        sys_div.append(x)

        
File=input("enter file name : ")

cmd_1=[]
for i in sys_div:
    try:
        cmd = sub.check_output("dir/ S/ B "+i+"\\"+File, shell=True).decode()
    except sub.CalledProcessError:
        pass
    if x in str(cmd):
        cmd_1.append(cmd)
for i in cmd_1:
    cmd=sub.check_output("del /S " +i+ "\\" +File, shell=True).decode()
