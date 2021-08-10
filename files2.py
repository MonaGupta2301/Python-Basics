file1="copy.txt"
file1="log.txt"

f=open('copy.txt')
data=f.read()
f.close()

f=open('log.txt')
data1=f.read()
f.close()
 
if(data==data1):
     print(" Files Are Same ")
else:
     print(" Files Are not Same ")