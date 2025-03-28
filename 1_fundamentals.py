# print ---> it is used to display information on the screen
#syntax
# print(exp)
# print(10+10)
# print("vasu kumar palani")
# Python standard library

# The Python Standard Library contains the exact syntax, semantics, and tokens of Python. It contains built-in modules that provide access to basic system functionality like I/O and some other core modules. Most of the Python Libraries are written in the C programming language. The Python standard library consists of more than 200 core modules. All these work together to make Python a high-level programming language. Python Standard Library plays a very important role. Without it, the programmers can’t have access to the functionalities of Python. But other than this, there are several other libraries in Python that make a programmer’s life easier. 


# builtins.py is a Python module that contains the built-in functions, exceptions, and objects that are always available in Python. These built-ins are accessible without explicitly importing them because they are part of the Python interpreter's core functionality.
# Purpose of builtins Module

#     Centralized Access: It defines and organizes functions, constants, exceptions, and classes that are essential for Python programs.
#     Always Available: The objects in builtins are automatically imported into every Python script, so you can use them directly.


# The builtins module is part of the Python Standard Library. It is implemented in C in CPython, so you won’t find a builtins.py file but can access its functionality through the Python interpreter.

#single line comments (#)
#below code is used to perform addition operation
# num_1 = 10 #here taken one variable and assign a value by using = operator
# num_2 = 10
# result = num_1 + num_2 #performed addtion operation by using + operator
# print(result)


'''
i have taken two variables
and i assigned values to those variables
and i perform addition operation by using + operator
later, i display the result by using print function

'''

"""
i have taken two variables
and i assigned values to those variables
and i perform addition operation by using + operator
later, i display the result by using print function

"""


#syntax
# variable = value
# user_id = 256789
# print(id(user_id))

# roll_number = 12345
# print(id(roll_number))

# _user = 57
# print(_user)
# _height = 5.7
# print(_height)

# 1st_user_id = 456  #invalid
# print(1st_user_id)

# _2nd_class = "grade"
# print(_2nd_class)

# gmail@id = "abc@gmail.com"
# print(gmail@id)


# __student___name = "priyanka"
# print(id(__student___name))
# STUDENT_NAME = "reddy"
# print(id(STUDENT_NAME))
# STUDENT_name = "sameul"
# print(id(STUDENT_name))

# if = 1234
# print(if)

# True = 57
# print(True)

# camelCase
# userName = "vasu"
# print(userName)

# #snake_case
# user_name = "anjali"

# #PascalCase
# UserName = "vamsi"
# print(UserName)



# age = 35
# print(type(age))

# number = 11111111111111111111111111155555
# print(type(number))


# height = 555.15
# print(type(height))

#strings used to represent textual information  and also it is used to store textual information
# sample_sentence = 'welcome to pythonlife '
# sample_sentence_2 = "welcome to pythonlife at 8'O clock "
# sample_sentence_3 = """ welcome to pythonlife he said, "join together 8'0 clock " 
# i have taken two variables
# and i assigned values to those variables
# and i perform addition operation by using + operator
# later, i display the result by using print function

# """
# print(sample_sentence)
# print(sample_sentence_2)
# print(sample_sentence_3)


# user_height = "5.7"
# print(user_height+50)

# num_1 = 25
# print(num_1+50)


# name = """ hello """
# print(name)

#int --> float
#type conversion --> two types --> implicit type conversion(automatic) and explicit type conversion(manual)
# number = 35
# print(number)
# print(type(number))
# float_conversion = float(number)
# print(type(float_conversion))


#float ---> int
# height = 5.7
# print(height)
# print(type(height))
# int_conversion = int(height)
# print(type(int_conversion))


# int ---> str
# age = 35
# print(age)
# print(type(age))
# str_conversion = str(age)
# print(type(str_conversion))

#str ---> int
# roll_number = "23456789"
# print(roll_number)
# print(type(roll_number))
# int_covnersion = int(roll_number)
# print(type(int_covnersion))


# str ---> float
# user_height = "578"
# print(user_height)
# print(type(user_height))
# float_conver = float(user_height)
# print(float_conver)
# print(type(float_conver))

# input function
# num_1 = float(input("enter the number: "))
# num_2 = float(input("enter the second number: "))
# result = num_1 + num_2
# print(result)

# num_1 = "hello"
# num_2 = "everyone"
# result = num_1 + num_2
# print(result)


# num_1=10
# num_2=5.7
# result=num_1+num_2
# print(result)


# age = input("enter something")
# print(age)




###########   march 07 2025  ############
# **Lists:**

# - A list is a mutable, ordered sequence of elements.
# - Elements can be of different data types.
# - Lists are defined using square brackets `[]`.
# list_1 = [35,5.7,"prathiba",(1,2,3),[1,2,3],1,1,1,1,2,2,2]
# print(list_1)
# print(id(list_1))
# list_1.append("pawanii")
# print(id(list_1))
# print(type(list_1))



# tuple_1 = (1,1,1,1,1,1,1,2,3,5.5,"kiran","vasu",[1,2,3,4],(1,2,3))
# print(type(tuple_1))
# print(tuple_1)
# print(id(tuple_1))




# set_1 = {11,123,1,2,3,"vasu",5.7,"pawanii","samuel",1,1,1,1,1,2,22,2,2,3,3,3,}
# print(set_1)

# set_1 = {11,5.7,"likitha",(1,2)}
# print(set_1)








# In Python, a complex data type is used to represent complex numbers. A complex number consists of a real part and an imaginary part, and it’s written in the form a + bj


# a → Real part (float or int)
# b → Imaginary part (float or int)

# sample = 4 + 5j
# print(type(sample))
# print(sample)
# a = 2 + 3j
# b = 1 - 4j
# print("Addition:", a + b)  


# accounts = {
#     "user1":"password1",
#     "user2":"password2",
#     "user3":"password3",
#     "user4":"password3",
#     1:123,
#     (1,2):5.7,
#     3:[1,2,3],
#     4:(1,2),
#     5:{1,2,3},
#     "user1":"vasu kumar",
# }
# print(accounts)
# print(type(accounts))




#boolean
# sample = True
# sample_1 = False
# print(type(sample))
# print(type(sample_1))


# print(bool(0))
# print(bool(1))







# sample_data = [1,2,3,4,5,1,2,3,4,"vasu","vasu","kumar","raju","priyanka"]
# print(sample_data)
# set_1 = set(sample_data)
# print(set_1)
# list_1 = list(set_1)
# print(list_1)

#int --> float
#float --> int
#str --> int
#int --> str
#list --> set
#set --> list


#list ---> tuple
#sets ---> tuple
#tuple --> list
#######  dict --> tuple #observe






#f -strings #string format
# num_1 = int(input("enter the number"))
# num_2 = int(input("enter the number"))
# # result = num_1 + num_2 
# # print(result)
# print(f"num_1 values is {num_1} and num_2 value is {num_2} and result is {num_1+num_2}")

# print("vasukumar"*3)


#7. **Type Conversions:**
    # - Convert a float to an integer and print the result.
# num_1 = float(input("enter  the number"))
# int_conversion = int(num_1)
# print(f"float values is {num_1} and converted to integer later value {int_conversion}")










# voter_list = ["vasu","tarun","sridevi"]
# emp_id = (123,456,789,)





# sample = ''' time is 8'o clock '''
# print(sample)
# why there is no error?
# - Declare two variables, one storing an integer and the other a string. Print their values.
# - Write a program that prints a pattern using multiple print statements.
# - Create a Python script for a simple task and add comments to explain each step.


# num_1 = 35 #take user age
# user = "krishna" #taken user name
# print(num_1)
# print(user)
# print(num_1,user)
# print(f"user name is {user} and age is {num_1}")

# print("------")
# print("-----------")
# print("-------------")
# print("-----------------")



# cost = 12
# man_fac = 2025
# fruits = "apple"
# print(f"i bought {fruits} and its cost {cost} and manfactured date {man_fac} ")


# price = 125
# price_1 = 99.05
# print(price+price_1)

