#errors  types
#1.syntax errors
#2. runtime errors
#3. logical errors ---> user need to be identified (very difficult to find these errors)

# num_1 = 10
# num_2 = 10
# print(num_1-num_2)


#1.syntax errors --> are the compile time errors
#for var in iter:
    #block of code


# for i in range(5):
#     print(i)


# for i in range(10):
#     print(i)

# while True:
#     print("hi")


#2. runtime errors ---> which disturbs the flow of execution ( during the execution ) also called exceptions
# num_1 = int(input("enter the number: "))
# num_2 = int(input("enter the number2: "))
# print(num_1+num_2)
# print(num_1-num_2)
# try:
#     print(num_1/num_2)
# except:
#     print("error has occured")
# print(num_1*num_2)
# print(num_1**num_2)


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# try:
#     print(my_list[9])
# except:
#     print("some error check index position")
# print(my_list[1]) #20
# print(my_list[4]) #50


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[4])
# try:
#     print(my_list[10])
# except:
#     print("some error occured")
# else:
#     print(my_list[3])
# finally:
#     print("regardless execution")


# try:
#     num_1 = int(input("enter the number: "))
#     num_2 = int(input("enter the number2: "))
# except ValueError as a:
#     print(a)
# else:
#     print(num_1**num_2)


# try:
#     num_1 = int(input("enter the number: "))
#     num_2 = int(input("enter the number2: "))
#     print(num_1/num_2)
# except Exception as e:
#     print(e)
    