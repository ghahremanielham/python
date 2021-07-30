#salam
#elham ghahremani tamrin9-3
import subprocess as sub
sys_div=[]
div=["A","B","C","D","E","F","G","H","I","Z","N"]
cmd = sub.check_output("net share",shell=True).decode()
for x in div:
    if x in str(cmd):
        sys_div.append(x)
print(sys_div)
