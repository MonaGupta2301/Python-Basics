#prime
num=int(input(" Enter Any Number :"))
prime=False
i=2
while i in range(2,num):
    if(num%i==0):
        prime=True
    if prime==True:
        print("\n Its Not An Prime Number ")
        break
    else:
        print("\n It is An Prime Number ")
        break