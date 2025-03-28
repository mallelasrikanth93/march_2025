#Syntax
# for variable in sequence:
    # code to be executed

# employee_data = ["sridevi","reddy","samuel","krishna","divya"]
# for item in employee_data:
#     print(f"{item} you are invited to the party. ")



# for i in "pythonlife":
#     print(i)


fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"{fruit} recevied")


# Syntax:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# for i in range(10):
#     print(i)

# for i in range(11):
#     print(i)


# for i in range(-9,10):
#     print(i)


# for i in range(10,21,1):
#     print(i)


# for i in range(0,11,3):
#     print(i)

#multiplication Tables
# for i in range(1,21):
#     print(f"2 X {i} = {i*2}")

# table = int(input("enter the table number: "))
# for i in range(1,11):
#     print(f"{table} X {i} = {i*table}")



#nested for loop

# for var in iterable:
#     for var2 in iterable:
#         #block of code

# for i in range(5):#outer for loop
#     for j in range(5):#inner for loop
#         print(i,j)



# for i in range(5):
#     print(i)


# for i in range(1,6):
#     for j in range(1,11):
#         print(f" {i} X {j} = {i*j} ")
#     print("-"*15)

# while condition:
#     # code to be executed

# while True:
#     print("pythonlife")


# age = 35
# while age>=18:
#     print("you are eligible to vote")


# count = 0
# while count<=4:
#     print(count)
#     count +=1


while True:
    user_name = input("enter username: ")
    password = input("enter password: ")
    if user_name == "manju" and password == "1234":
        print("login success........")
        break
    else:
        print("invalid login credentials")


# Syntax:
# while outer_condition:
#     # outer loop code
#     while inner_condition:
#         # inner loop code

# Example:
# outer = 0
# while outer < 3:#outer condition
#     inner = 0
#     while inner < 2:#inner condition
#         print(outer, inner)
#         inner += 1
#     outer += 1




# while True:
#     print("welcome to pythonlife")
#     while True:
#         print("hello everyone welcome to pythonlife")
#         break
















