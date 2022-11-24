import datetime
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

    @classmethod
    def set_pay_raise(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def srom_string(cls,emp_string):
        first,last,pay =emp_string.split('/')
        return cls(first,last,name)

    @staticmethod
    def is_work_day(day):
        if day.weekday() in[5,6]:
            return False
        return True


Employee.set_pay_raise(1.1)
emp1=Employee('Jack','Smith', 3000)
emp2=Employee('Mary','Gold', 3200)
emp_str='Bbob/Ssmith/22500'
f,l,p = emp_str.split('/')
emp3=Employee(f,l,p)
print(emp1.raise_amount)
print(emp3.__dict__)
print(Employee.raise_amount)

print(Employee.is_work_day(datetime.date(22,11,12)))