class Employee:

    raise_amount =1.4

    def __init__ (self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
    @property
    def email(self):
        return (    self.first+'.'+self.last+'@companymname.com').lower()

    @property
    def fullname(self):
        return f'{self.first.title()} {self.last.title()}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print('Name deleted')
        self.first = None
        self.last = None



    def pay_raise(self):
        self.pay=int(self.pay*1.04)

    @classmethod
    def set_pay_raise(cls,amount):
        cls.raise_amount=amount

    def __str__(self):
        return f'{self.fullname}, {self.pay}EUR'

    def __repr__(self):
        return f'Employee(\'{self.first}\',\'{self.last}\',{self.pay})'

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len (self.fullname) -1

emp1=Employee('Jack','Smith', 3000)
emp2=Employee('Mary','Gold', 3200)

print(emp1)
print(emp1 + emp2)
print(len(emp1))

print(int.__add__(5,2))
print(str.__len__('Hello world'))
print(str.__add__('hello','people'))
print(emp1.fullname)
print(emp1.email)


del emp1.fullname
print(emp1.__dict__)
emp1.fullname= 'Roman Kutselepa'
print(emp1.__dict__)
