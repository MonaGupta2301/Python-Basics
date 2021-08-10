
class employee:
    company="google"


mona=employee()
prabhu=employee()
print(mona.company)
print(prabhu.company)
employee.company="youtube"
print(mona.company)
print(prabhu.company)
print(employee.company)
