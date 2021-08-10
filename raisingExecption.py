try:
    a=int(input(" Enter the Value of A :"))
    print(a)
except Exception as e:
    print(" You Were Typed Wrong")
    exit()
finally:
    print(" We Were Successfull ")