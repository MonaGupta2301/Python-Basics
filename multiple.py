class base1: 
    name="Mona Gupta"
    def printname(self):
        print("\n Your name Is : ",self.name)
        return 0
class base2:
    roll=100
    def printrollnum(self):
        print("\n Roll Num is : ",self.roll)
        return 0

class derive(base1,base2):
    address="sai nagar amravati"
    def printadd(self):
        print("\n Address is : ",self.address)
        return 0

mult=derive()
mult.printname()
mult.printrollnum()
mult.printadd()