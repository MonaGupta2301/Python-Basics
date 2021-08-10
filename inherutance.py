class base:
    company="google"
    def basefun(self):
        print(" Thes Is Base Function")
        return 0
    
class derive(base):
    language="python"
    def derivefun(self):
        print(" these is Derive function")
        return 0
    # def basefun(self):
    #     print(" Thes Is Base Function2")
    #     return 0
    
    


b=base()
d=derive()
d.basefun()
d.derivefun()