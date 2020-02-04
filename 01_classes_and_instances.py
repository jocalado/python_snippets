#!/usr/bin/python

""" Python OOP Tutorial 1: Classes and Instances"""

# INSTANCE VARIABLES
# Use Case: Add a New Employee to a HR database

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Joana','Calado',100000)
emp_2 = Employee('User','Test',80000)

# Print Employee 1 FullName
print(emp_1.fullname())
