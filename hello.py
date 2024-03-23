# # # todo later
# # # multiline is the same
# # # print("hello!") # inline in comment

# # # numeric
# # o = 10 # integer
# # a = 10.0 # float
# # k = o + 9 * a # complex

# # # sequence types
# # j = 'rueowp' #strings
# # i = [1,2,3, "9", '-'] # list, like an array in js
# # h = ('45', 34, 10.0) # tuple, similar to lists, but immutable

# # # dictionary
# # x = {a: 'a'} #like objects?

# # # boolean
# # q = (10 == 10) #True
# # 10 < 5 #False

# # # sets
# # m = {6, '4', 1.9} same as lists(array), but in curly

# # # multiline 

# # string = "this is \
# # a very \
# # long \
# # sting"

# # name = "Assel"
# # anotherName = "Aselle"
# # # print(type(str)) # prints out the data type
# # # print (anotherName[1])

# # # print("Where do you live?")
# # #location = 
# # # input() # captures input
# # # someLen = 
# # len(m) # length
# # str() # converts into string
# # int() # converts into int
# # float() # converts to float
# # # print("So you live in " + location)

# # def someIdentifier():
# #     return 'yoyo'

# # def someId(you):
# #     return 'hello ' + you

# # email = input('give me your email: ')
# # print('your email is: '+email)
# # print('i like {0} more than {1}'.format('oranges', 'grapes'))
# # print('hello', 'you', sep='--')

# # # object
# # # sep
# # # end 
# # # file
# # # flush

# # # Using explicit type conversion, change the following 
# # # inputs so the types match with the following below
# # #  
# # # name = type string
# # # age = type int
# # # height = type float
# # # loyalty = type boolean

# # # Modify the line below
# # # Using explicit type conversion, change the following 
# # # inputs so the types match with the following below
# # #  
# # # name = type string
# # # age = type int
# # # height = type float
# # # loyalty = type boolean

# # # Modify the line below
# # # name = input('What is your name? ')

# # print("Type of name variable is: {type(name)}. It should be <class 'str'>")

# # # Modify the line below
# # # age = int(input('What is your age? '))

# # print("Type of age variable is: {type(age)}. It should be <class 'int'>")

# # # Modify the line below
# # # height = float(input('What is your height in meters? '))

# # print("Type of height variable is: {type(height)}. It should be <class 'float'>")

# # # Modify the line below
# # # loyalty = bool(input('Are you part of our loyalty program? '))

# # #print(f"Type of loyalty variable is: {type(loyalty)}. It should be <class 'bool'>")


# # a = True
# # b = True
# # if a and b:
# #    # print('all true')   

# # # if elif else
# #     http_status = 404
# # if (http_status == 200 or http_status == 201):
# #     print('success')
# # elif http_status == 400:
# #     print('bad request')
# # elif http_status == 404:
# #     print('page not found ')
# # else: print('unknown error')

# # # same as above in a match versuin
# # match http_status:
# #     case 200 | 201:
# #         print('yay')
# #     case 400:
# #         print('bad request')
# #     case 404:
# #         print ('not found')
# #     case _: # equivalent to 'everything else'
# #         print('unknown')
        

# # for i in range(10):
# #     print('looping through', i)

# # favorites = ['macarons', 'croissants', 'tiramisu', 'carrot cake']
# # for index, item in enumerate(favorites):
# #     # print (index, item)
# #     if ( item == 'tiramisuu'):
# #         print('yay! you have', item)
# #         break
# #     else: 
# #         print('no desert for you')

# count = 0

# # while count < len(favorites):
# #     print('i like dessert', favorites[count])
# #     count+=1


# # favorites = ['macarons', 'croissants', 'tiramisu', 'carrot cake']
# # for item in favorites:
# #     # print (index, item)
# #     if item != 'macarons':
# #         print('no desert for you')
# #     else: 
# #         print('yay! you have', item) # how to make it correct? run once when it's not satified, false?

# # import time # time library or library



# # k = input(" y")
# # print(k)

# # def total(bill, tax):
# #     return (round(bill*tax)/100.00, 2)
# # print('total tax',(total(125, 15.17)))

# # scoping LEGB
# # Local, Enclosing, Global, Built-in

# # ilist = [1,2,3]
# # print(*ilist) # prints out the whole list, raw
# # print(ilist) # prints out the whole list, as a list w []
# # print(ilist, sep = "**") # prints out the whole list, as a list w []
# # ilist.insert(len(ilist)-3, 4) # first is the index num where to place, second is the value itself
# # print(*ilist)

# # ilist.append(7) # appends to the end of the list
# # print(*ilist)

# # ilist.extend([9,6,4]) # adds to the list, must be in []
# # print(*ilist)

# # ilist.pop(0) # removes specified index
# # print(*ilist) 

# # del ilist[3]
# # print(*ilist) # removes spefified index

# # for x in ilist:
# #     print(x)

# # sometup = 1, '5', True, [5,7,1], '5' # mixed val of tuples
# # print(sometup.count('5')) # counts how many '5' in tuple
# # print(sometup.index('5')) # show an index of '5', first

# # for i in sometup:
# #     print(i)

# # someSet = {1,6,3,9,3,8,0}
# # someSet.add(76)
# # print(someSet)
# # someSet.remove(6) # by value
# # print(someSet) # removes value 6
# # someSet.discard(1) # by value, same as remove
# # print('final set', someSet)

# # anotherSet = {9,11,7,4,0,1}
# # print('second set:', anotherSet)

# # print('union     ', someSet.union(anotherSet)) # merges 2 sets
# # print('also union', someSet | anotherSet) # also merges 2 sets 
# # print('intersection     ', someSet.intersection(anotherSet)) # shows commong values
# # print('also intersection', someSet & anotherSet) # also shows commong values
# # print('difference in first set     ', someSet.difference(anotherSet)) # shows items in first union that are not in second
# # print('also difference in first set', someSet - anotherSet) # shows items in first union that are not in second
# # print('difference in both sets     ', someSet.symmetric_difference(anotherSet)) # shows items in first and second, not in common
# # print('also difference in both sets', someSet ^anotherSet) # shows items in first and second, not in common


# # thirdSet = {1,1} # no duplicate values!
# # thirdSett = {74, 74}
# # print(thirdSett)

# # # dictionaries

# # myD = {7: 'value', 'another': 'op', 4:9, True: False} # can be mixed values
# # print(myD[7])

# # for x in myD:
# #     print('my D: ',x, ':', myD[x])


# # for key, values in myD.items():
# #     print('key: ',key, ':', values)

# # args kwargs

# def someFun(x,y):
#     return x+y
# # print(someFun(2,5,8)) # error: takes 2 positional arguments but 3 were given

# args, takes in any amount of arguments
# def someFun2(*args): # takes in n number of args
#     sum = 0
#     for x in args:
#         sum += x
#     return sum
# print(someFun2(2,6,8,76))

#kwargs takes in any amount of key-value arguments
# def kwarg(**kwargs):
#     sume = 0
#     for k, v in kwargs.items():
#         sume +=v
#     return sume
# print('total for breakfast:', kwarg(coffee=5.23, bread=3.56, smoothie=8.11))

# import time
# startTime =time.time() # starts time when script it running
# employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]

# def get_employee(id):
#     for employee in employee_list:
#         if employee[0] == id: # why 0?
#             return {"id": employee[0], "name": employee[1], "department": employee[2]}

# print(get_employee(12458))

# print(round((time.time()-startTime),2)) # to count the time for complexity

# def div(a,b):
#     return a / b

# forty = div(40,0) # error

# to catch errors
# try:
#     forty = div(40,0)
# except ZeroDivisionError as e:
#     print(e, ', we can not divide by zero') # prints out error messages
#     # print(e.__class__)
# except Exception as e:
#     print(e, 'something went wrong') # to catch chain multiple errors, chain together


# def divide_by(a, b):
#     # return a / b
#     try:        
#         return a / b
#     except ZeroDivisionError:
#         return 0
#     except Exception as e:
#         print(e, ', we can not divide by zero') # prints out error messages

# file handling functions:
# open(name/location, mode(like, read, write, creating editing/appening data))
        
# r open and read
# rb reading in binary
# rb+ r and w
# w writing, overrides
# a append or edit
# with open() as file: -- another way to open function
# close() used for clsoing open file connections
        
# file = open('test.txt', mode='r') # reads test.txt file
# data = file.readline()
# print(data)
# file.close()

# better way to open file, closes also
# with open('test.txt') as file:
#     data = file.readline()
# print(data)

# with open('newtxt.txt', 'w') as file:
# with open('newtxt.txt', 'a') as file: # appends, adds to the file
#     # file.write('this is some new data') # after running, new file generates
#     file.writelines(['\nthis is through file.wrtielines', '\nanother one']) # after running, new file generates

# to handle an error of non-existing files or directories
# try:
#     with open('sample/newtxt.txt', 'a') as file: # appends, adds to the file
#         file.writelines(['\nthis is through file.wrtielines', '\nanother one']) # after running, new file generates 
# except FileNotFoundError as e:
#     print('Error', e)


# read() reads whole file
# read(44) reads first 44 characters
# readline() reads first line
# readlines() returns a list of lines

# with open('newtxt.txt', 'r') as file:
#     for x in file:
#         print(x)

# with open('pets.txt', 'w') as file:
#     file.writelines('')

# with open("petnames.txt", "r") as f:
#     for names in f:
#         nn = names.split("")
#         print(nn)

# import random

# f = open('petnames.txt', 'r') # opens file
# names = f.read() # reads the file and saves content into names
# nn = names.split("\n") # turns into a list
# f.close()
# # print(nn)

# print(random.choice(nn)) # takes in a list, gives random


# list = []
# # f_name = input('petnames.txt','r')
# f = open('petnames.txt')

# f_content = f.read()
# # for x in f_content:
#     # print(f_content)
# nn = f_content.split("\n")
#     # list.append(x)
# print(nn)

# with open('petnames.txt', 'w') as file:
#     file.writelines('some name')
#     print('petnames.txt')

# new_list = [1,2,3,4]


# new_list[4] = 10


# new_list.extend(new_list)


# new_list.insert(0, 0)


# new_list.append(5)

# print(new_list)

# to reverse in python with slice:
# str[start:stop:step]
# str = 'something'
# newstr = str[::-1] #start from the end, move -1 backwards
# print(newstr)

# to reserse with recursion:
# def rec(str):
#     if len(str) == 0:
#         return str # base case
#     else:
#         return(rec(str[1:])+str[0])
    

# str = "tux"
# reversed = rec(str)
# print(reversed)

# map() and filter()
# menu = ['espresso', 'cortado', 'capuccino']

# def findCof(coffee):
#     if coffee[0] == 'c':
#         return coffee
    
# mapCofee = map(findCof, menu)
# print(mapCofee) #prints out the memory location
# for x in mapCofee:
#     print(x) #prints all values, none for false too
    
# filterCofee = filter(findCof, menu)
# print(filterCofee)
# for x in filterCofee:
#     print(x) # prints out only the values

# LIST comprehension
# data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
# data = [x+3 for x in data] # adds 3 to each val
# print("Updating the list: ", data) 
# new_data = [x*2 for x in data] # new list x2 each
# print("Creating new list: ", new_data) 
# fourx = [x for x in new_data if x%4 == 0 ]
# print("Divisible by four", fourx)
# fourxsub = [x-1 for x in new_data if x%4 == 0 ]
# # print("Divisible by four minus one: ", fourxsub)
# nines = [x for x in range(100) if x%9 == 0]
# print("Nines: ", nines)
    
# DICTIONARY comprehension
# usingrange = {x:x*2 for x in range(12)}
# print("Using range(): ",usingrange)
# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]
# # numdict = {x:x**2 for x in number}
# # print("Using one input list to create dict: ", numdict)
# months_dict = {key:value for (key, value) in zip(number, months)}
# print("Using two lists: ", months_dict)

# SET comprehension
# set_a = {x for x in range(10,20) if x not in [12,14,16]}
# print(set_a)

# GENERATOR comprehension
# data = [2,3,5,7,11,13,17,19,23,29,31]
# gen_obj = (x for x in data)
# print(gen_obj)
# print(type(gen_obj))
# for items in gen_obj:
#     print(items, end = " ")

# z = ["alpha","bravo","charlie"]
# new_z = [i[0]*2 for i in z]
# print(new_z)

# a = [[96], [69]]
# print(''.join(list(map(str, a))))

# dict = {key:value for (key,value) in zip(emplpoyee_list[0]["name"][0],employee_list[0]["id"])

def sum(n):
   if n == 1:
       return 0 # after reaching the base case 0,
   return n + sum(n-1) # starts "unwinding the call stack" process
    # stored in the activation records on the call stack
    # then retrieved during the unwinding process
a = sum(5) 
print(a)

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
small = list(map(lesser, numbers))
print(small)