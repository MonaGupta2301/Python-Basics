a={12,23,34,45,67,78}
print(a)

# Its Not An Empty Set Its An Empty Dictionay
#  a={}
#  print(a)
#  print(type(a))
 
b = set()
b.add(21)
b.add(26)
b.add(22)
b.add(29)
b.add(72)
b.add(42)
b.add((12,23,34))
print(b)

#length function
print(len(b))

#remove Function
b.remove(21)
print(b)

#pop Function
b.pop()
print(b)

b.pop()
print(b)
 
# b.clear()
# print(b)

b.union({12,23,22,89})
print(b)

b.intersection({12, 90})
print(b)
