#global variable
a=200
def fun1():
    global a
    print(a)
    a=300
    print(a)

fun1()
print(a)