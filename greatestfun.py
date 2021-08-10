def greatest(a,b,c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
         if(b>c):
            return b 
         else:
            return c


a=int(input("\n Enter 1st Num : "))
b=int(input("\n Enter 2nd Num : "))
c=int(input("\n Enter 3rd Num : "))
a1=greatest(a,b,c) 
print(f" Greater Number Between 3 numbers Is {a1}")