class Employee:

    raise_amount = 1.04
    num_of_ems=0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last +'@company.com'
        Employee.num_of_ems+=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)



emp_1 = Employee('Sam','Sundar',80000)
emp_2= Employee('Test','User',5000)
emp_3 = Employee('Sam','Sundar',80000)
emp_4= Employee('Test','User',5000)
emp_6 = Employee('Sam','Sundar',80000)
emp_5= Employee('Test','User',5000)
emp_1.raise_amount=1.04
Employee.raise_amount=1.05
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_ems)

