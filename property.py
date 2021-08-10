class employee:
    salary=5600
    bonus=500

    @property
    def totalsal(self):
        return self.salary+self.bonus

e=employee()
print(e.totalsal)    
    