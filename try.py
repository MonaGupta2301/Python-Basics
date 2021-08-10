print("\n Press q to Quite ")
while(True):
    a=input(" Enter a Number :")
    if(a=='q'):
        print("Thanks To Play Thes game")
        break
    try:
        a=int(a)
        if(a>10):
            print(" A is greater Then 10")
        else:
            print(" A ids less then 10")
    except Exception as e:
        print(f" The Value Which you Enter is inccorct :")