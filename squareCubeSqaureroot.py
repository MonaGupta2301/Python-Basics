class addition:
    @staticmethod
    def square(a):
        print(f"\n Square of a Given Number Is : {a **2}")
        return 0
    @staticmethod
    def cube(a):
        print(f"\n cube of a Given Number Is : {a **3}")
        return 0
    @staticmethod
    def square_root(a):
        print(f"\n Square Root of a Given Number Is : {a **0.5}")
        return 0


a=int(input("\n Enter Any Number : "))
mona=addition()
mona.square(a)
mona.cube(a)
mona.square_root(a)