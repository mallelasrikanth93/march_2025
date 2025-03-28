#Syntax
# def funcname():
#     #block of code
#     #block of code


# def greet():
#     print("hello welcome to pythonlife")
#     num_1 = 10
#     num_2 = 20
#     print(num_1+num_2)
# greet()

# def list_1():
#     my_list = [10, 20, 30, 40, 50, 60, 70, 80]
#     print(my_list[4:7])#50 60 70
#     print(my_list[-4:-1])#50 60 70
#     print(my_list[6:3:-1])#70 60 50
# list_1()



# def details():#function definition
#     user_name = "sandeep" #function body
#     id = 1234 #function body
#     print(f"username is {user_name} id is {id}") #function body
# details()#function calling


# def add(num_1,num_2): #function definition
#     print(num_1+num_2)
# add(5,5)#function calling 


# def details(user,id):#function definition
#     print(user)
#     print(id)
# details("kiran",25)
# details("vasu",29)
# details("srinu",35)


# def sample(a):
#     print(a)
# sample("vasu")




# def myfunc(a,b):
#     return a+b
# print(myfunc(10,10))


# def sub(a=None,b=None,c=None):
#     print(a,b,c)
# sub("kiran","pavan","vasu")
# sub("sandeep","divya")
# sub("sridevi")
# sub()



# def power(base, exponent=2):
#     return base ** exponent

# print(power(3)      )
# print(power(3, 4) )

# #arbitary arguments--> function can accept a variable number of arguments by using *args(syntax)
# def details(*a):  #* --> all
#     print(a)
# details("vasu","kumar","raju","kiran")

#*--> tuple

# a = "vasu","kumar","raju","kiram"
# print(a)


#keyword arguments :-->keyword arguments are passed to a function with a keyword and a value, allowing for more explicit parameter passing
#**
# def sample(**a):
#     print(a)
# sample(a=1,b=2,c=3)

# * --> tuple
# ** --> dict




# variables ---> two types
#local variables --> function (inside the function)
#global variables --> A variable declared outside of all functions and accessible throughout the program, including inside functions, is called a global variable.


# def greet():
#     name = "sandeep"#local variable
#     dept = "frontend" #local variable
#     id = 1234
#     print(name)
#     print(dept)
#     print(id)
#     print(id*12)
# greet()

# balance = 1000 #global variable
# def credit(amount=0):#function definition
#     global balance
#     balance+=amount
#     print(f"credited amount {amount}")
#     print(f"total balance {balance}")
# credit()
# print(balance)




# def add(a,b):
#     print(a+b)
# def sub(a,b):
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def expo(a,b):
#     print(a**b)
# add(5,5)
# add(5,5)
# add(25,20)
# sub(10,5)




# #ATM
# balance = 1000
# def credit():
#     pass
# def withdraw():
#     pass
# def balance():
#     pass
# def exit():
#     pass






























# age = 35
# def sample():
#     global age
#     age += 18
#     print(age)
# sample()



#import modulename
# modulename.func()



