from functools import reduce
l=[1,2,3,4,5]
summ=lambda a,b : a+b
value=reduce(summ,l)
print(value)