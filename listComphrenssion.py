a=[12,23,34,34,12,15,34,56,67,45,67,89,90]
# b=[]
# for  i in a:
#     if i%2==0:
#         b.append(i)

b=[i for i in a if i%2==0]
print(b)
