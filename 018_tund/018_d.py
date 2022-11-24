class Employee:

    raise_amount =1.4

    def __init__ (self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=(first+'.'+last+'companymname.com').lower()


    def fullname(self):
        return f'{self.first.title()} {self.last.title()}'

    def pay_raise(self):
        self.pay=int(self.pay*1.04)

    @classmethod
    def set_pay_raise(cls,amount):
        cls.raise_amount=amount

class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        #Employee.__init__(self, first, last, pay)
        super().__init__(first,last,pay)
        self.prog_lang =prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay,)
        if employees is None:
            self.employees=[]
        else:
            self.employees =employees

    def add_employee (self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee (self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
    def print_employee(self):
        for emp in self.employees:
            print(emp.fullname())

emp1=Employee('Jack','Smith', 3000)
emp2=Employee('Mary','Gold', 3200)
dev1=Developer('Bob','Summer',5000, 'Pyt')
man1=Manager('Sarah','Brown',5000,[emp1,emp2,dev1])

print(dev1.__dict__)
print(man1.__dict__)
print(man1.employees[2].fullname())

print(type(emp1))
print(type(dev1))

for emp in man1.employees:
    print(emp.fullname())

man1.add_employee(emp1)
man1.remove_employee(emp1)
print(man1.employees)
man1.print_employee()

print(isinstance(man1,Manager))
print(isinstance(man1,Developer))
print(isinstance(man1,Employee))
print('+++++')
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Employee, Developer))