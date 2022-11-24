class Employee:

    number_of_employees=0

    def __init__ (self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=(first+'.'+last+'companymname.com').lower()
        Employee.number_of_employees += 1

    def fullname(self):
        return f'{self.first.title()}{self.last.title()}'

    def pay_raise(self):
        self.pay=int(self.pay*1.04)

emp1=Employee('Jack','Smith', 3000)
emp2=Employee('Mary','Gold', 3200)
print(emp1.first)
print(emp1.email)
print(emp1)
print(emp2.last)

print(emp1.fullname())
print(Employee.fullname(emp2))
print(emp1.__dict__)
print(emp1.number_of_employees)



print(emp1.pay)
emp1.pay_raise()
print(emp1.pay)
print(emp1.__dict__)
print(Employee.__dict__)
# emp2=Employee()
#emp1= Employee()
# emp1.first='Jack'
# emp1.last='Smith'
# emp1.email ='jack.smith@hot.ee'
# emp1.pay = 3000
# print(emp1.email)

