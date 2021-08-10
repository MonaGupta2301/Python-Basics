class c2vector:
    def element(self,num1,num2):
        self.num1=num1
        self.num2=num2
        return 0

    def sum(self):
        add=self.num1+self.num2
        return add

class d2vector(c2vector):
    def element1(self,num3):
        self.num3=num3
        print(f" third num is Num is :{num3}")
        return 0


d2=d2vector()
b=d2.element(10,20)
a=d2.sum()
print(f" Addition is :{a}")
d2.element1(100)