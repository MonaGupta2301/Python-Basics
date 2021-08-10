def openfile(filename):
    try:
        with open(filename,"r") as f:
            print(f.read())
    except Exception as e:
        print(" File Note Present")

openfile("1.txt")
openfile("2.txt")
openfile("3.txt")