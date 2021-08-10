l=[1,2,3,4,5,6,7,8,7,8,9,8,9,89,987,89,7]
num=lambda num:num<10
print(list(filter(num,l)))
g10=lambda num:num>10
print(list(filter(g10,l)))

