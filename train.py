class train:
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare

    def getinfo(self):
        print(f" The Name Of Train Is : { self.name}")
        print(f" The Seats Of Train Is : { self.seats}")
        return 0

    def getfare(self):
        print(f" The fare Of Train Is : { self.fare}")
        return 0
    
    def ticketbook(self):
        if(self.seats>0):
            print("\n Your seats Are Booked ")
            self.seats=self.seats-1
        else:
            print("\n Seats Are not Available")
    def canceltiket(self):
        if(self.seats>0):
            self.seats=self.seats+1
            print(f" Seats Cancelled {self.seats}")
        else:
            print(" Seats Are empty")


inter=train("Chinai Express Num : 234432 ", 430,100)
inter.getinfo()
inter.getfare()
inter.ticketbook()
inter.getinfo()
inter.canceltiket()
inter.getinfo()
        