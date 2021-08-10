# Sum Of First N Natural Number 
n=int(input(" Enter Any Number :"))
i=1
fact=1
for i in range(1,n+1):
    fact=fact*i 
    i=i+1

print(f"\n Factorial Of {n} Is {fact}")
