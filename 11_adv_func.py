#syntax
# lambda arguments: expression

# def add(a,b):#function definition
#     return a+b
# print(add(10,10))

# result = lambda a,b:a+b
# print(result(10,10))


# result = lambda a,b,c:a*b*c
# print(result(5,5,5))



# Syntax:
# filter(function, iterable)

# list_1 = [1,2,3,4,5,6,7,8,9,10]
# empty_list= []
# for i in list_1:
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)


# filter(function, iterable)
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# def even(a):
#     return a%2==0
# obj = filter(even,list_1)
# print(list(obj))

# #lambda arg:exp
# filter(fun,iter)
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# result = filter(lambda i:i%2==0,list_1)
# print(list(result))



# result = filter(lambda i:i%2==0,[1,2,3,4,5,6,7,8,9,10])
# print(list(result))


	# Syntax:
	# map(function, iterable, ...)

# list_1 = [1,2,3,4,5,6,7,8,9,10]
# empty_list = []
# for i in list_1:
#     result = i**2
#     empty_list.append(result)
# print(empty_list)



# map(function, iterable, ...)
#task --> take inputs as more iterables
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# def square(i):
#     return i**2
# result = map(square,list_1)
# print(list(result))


#  lambda arg:exp
# #  map(function, iterable, ...)
# list_1 = [1,2,3,4,5,6,7,8,9,10]
# result = map(lambda i:i**2, list_1)
# print(list(result))



# Syntax:
# from functools import reduce
# reduce(function, iterable[, initializer])#initializer--optional


# def add(a,b):
#     return a+b
# from functools import reduce
# result=reduce(add,[1,2,3,4,5,6,7,8])
# print(result)


# from functools import reduce
# result = reduce(lambda a,b:a+b,[25,25,35,45,55])
# print(result)



# def add():
#     return 1+2

# print(add())

"""
generator function --  a genetor -function is defined like a normal function
but whenever its need to generate a value
it does so with the yeild keyword rather than return
if body contain yield , the function  automatically
becomes a generator function.
"""

# def sample():
#     yield 1 #pause or hold
#     yield 2 #pasue or hold
#     yield 3 #pause or hold
# obj = sample()
# print(obj.__next__())
# print(obj.__next__())
# print(obj.__next__())

