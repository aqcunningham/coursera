# # class object
# class myClass:
#     a = 5
#     # pass # a placeholder when nothing needs to be executed
#     # print("yello")

#     # method object
#     def hell(self):
#         print("something")


# # instance object
# instanceObj = myClass()
# print(instanceObj.a)
# print(myClass.a) # works the same as above
# print(instanceObj.hell())

'''above is instantionaion:
1. class definition
2. creating new instance
3. initializing new instance'''


# class Receipe:
#     # # method 1
#     # def __new__(cls) -> Self:
#     #     pass

#     # # method 2
#     # def __init__(self) -> None:
#     #     pass

#     def __init__(self, dish, items, time) -> None:
#          self.dish = dish
#          self.items = items
#          self.time = time

#     def contents(self):
#         print("the " + self.dish + " takes " + str(self.items) + "to cook " + str(self.time)) 

# pizza = Receipe("Pizza", ["bread", "cheese", "sauce"], 45)

# print(pizza.items)
# print(pizza.contents())

# lab
# class MyFirstClass:
#     print('Who wrote this?')
#     index = 'Author-Book'

#     def hand_list(self, philosopher, book):
#         print(MyFirstClass.index)
#         # self.philisopher = "Plato"
#         # self.book = "Republic"
        
#         print(philosopher + " wrote the book: " + book)

# #  instantiate an object of that class
# whodunnit = MyFirstClass()

# # print(whodunnit.hand_list("Sun Tzu", "The Art of War"))
# whodunnit.hand_list("Sun Tzu", "The Art of War")


# class paySlips():
#     # init function
#     def __init__(self, name, payment, amount) -> None:
#         self.name = name # variables
#         self.payment = payment
#         self.amount = amount

#     # function 
#     def pay(self):
#         self.payment = "yes"

#     #function
#     def status(self):
#         if (self.payment) == "yes":
#             return self.name + " is paid " + str(self.amount)
#         else:
#             return self.name + " is not paid"
        
#instances:
# nathan = paySlips("Nathan", "no", 1000)
# print(nathan.status()) 
# george = paySlips("George", "yes", 2000)
# print(george.status()) 
# nathan.pay() # acts as swith on
# print(nathan.status()) 

# class employees:
#     def __init__(self, name, last) -> None:
#         self.name = name
#         self.last = last

# class supervisoirs(employees):
#     def __init__(self, name, last, password) -> None:
#         super().__init__(name, last)
#         self.password = password

# class chefs(employees):
#     def leave_days(self, days):
#         return "May I leave for " + str(days) + " days?"
    
# someinst = employees("Lisa", "J")
# adrian = supervisoirs("Adrian", "G", "prada")
# emily = chefs("Emily", "E")
    
# print(emily.leave_days(3))
# print(adrian.password)
# print(emily.last)

# boolean realtions:
# print(issubclass(supervisoirs, employees)) # supervisoirs is a subclass of employees
# print(isinstance(someinst,employees)) # determines if some object is an instance of some class. someinst is an instantiated obj of employees class

# super() acesses parent or sibling classes
# class Fruit():
#     def __init__(self, fruit):
#         #print('Fruit type: ', fruit)
#         pass

# class FruitFlavour(Fruit):
#     def __init__(self):
#         super().__init__('Apple')
#         print('Apple is sweet')

# apple = FruitFlavour()

from abc import ABC, abstractmethod

# class someAbstraction(ABC):
#     @abstractmethod #decorator
#     def someAbsMethod(self):
#     pass

# class employee(ABC):
#     @abstractmethod
#     def donate(self):
#         pass

# class donation(employee):
#     def donate(self):
#         a = input("how much?")
#         return a

# amounts = 0

# # employee instances
# jonah = donation() # instationate a class to an obj
# j = jonah.donate()
# amounts += int(j)

# peter = donation() # instationate a class to an obj
# p = peter.donate()
# amounts += int(p)

# print('donated total: ', amounts)
# @abstractmethod
# class A:
#     a = 5
# @abstractmethod
# class B(A):
#     b = 6
# @abstractmethod

# class C(B):
#     c = 7
# mro Method Resolution Order
# print(C.mro()) # suppose to print the chain of dependent and inhereted classes
# print(C.help()) # provides a lot of info about connections
# class A:
#    def a(self):
#        return "Function inside A"

# class B:
#     def a(self):
#         return "Function inside B"

# class C(A, B):
#     pass

# # Driver code
# c = C()
# print(c.a())
# bravo = 3
# b = B()
# class B:
#     bravo = 5
#     print("Inside class B")
# c = B()
# print(b.bravo) # an error - B in line 187 not defined


# modules
# any py file can be a module

# import sys
# location = sys.path
# # print(location)
# for i in location:
#     print(i)

# import calendar
# lp = calendar.leapdays(1950, 2024)
# isit = calendar.isleap(2024)
# print(lp, isit)

# sys.path.insert(1, r'/Users/aqcunningham/Documents/cmb/hello.py')
# import hello # file hello.py
# print(hello.numbers) # variable numbers with a list

# # import math
# from math import sqrt # better than above, bcz only selected piece requested, saves memory

# # modules saved as alias:
# import math as m
# cosine = m.cos(0)
# print(cosine)

# # selective import as alias
# from math import factorial as f
# fac = f(9)
# print(fac)

# # selective import
# from math import log10, sqrt

# from math import *

# maniluplating locality and globality of scopes:

def d():
    animal = 'elephant'
    def e():
        nonlocal animal
        animal = 'giraffe'
        print('1. inside the nested fun: ' + animal)
    print('2. before calling function: '+animal)
    e()
    print('3. after nested function: '+ animal)
animal = 'camel'

d()
print('4. global animal: '+animal)

