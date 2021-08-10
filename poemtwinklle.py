f=open('poem.txt')
data=f.read()
if 'Twinkle' in data :
    print(" Twinkle Is Present In Text File")
else:
    print(" Twinkle Is Not Present in text File ")

f.close()