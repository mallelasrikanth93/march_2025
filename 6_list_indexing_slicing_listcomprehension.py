# list_1 = []
# print(type(list_1))

# list_2 = [1,2,3,5.7,"pythonlife",{1:123}]
# print(type(list_2))

# list_3 = list()
# print(type(list_3))


# list_1 = [1,2,3,4,5,6]
# #syntax
# # var[index]
# print(list_1[3]) #4
# print(list_1[1]) #2
# print(list_1[5]) #6
# print(list_1[-6]) #1
# print(list_1[-1]) #6


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# #seq[s:s:s]
# # print(my_list[1:7])
# # print(my_list[0:4])
# # print(my_list[3:6])
# print(my_list[0:8])
# print(my_list[:8])
# print(my_list[:])
# print(my_list[::])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[1:])
# print(my_list[:3])
# print(my_list[::-1])


# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[4:7])#50 60 70
# print(my_list[-4:-1])#50 60 70
# print(my_list[6:3:-1])#70 60 50
# print(my_list[4:1:-1])#70 60 50
# print(my_list[-2:-5:-1])#70 60 50

# my_list = [10, 20, 30, 40, 50, 60, 70, 80]
# print(my_list[::4])

#syntax
#.methodname()
#.methodname(args)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers)
# numbers.append(["pythonlife","vasu","pavan"])
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.extend(["vasu","kiran","sameul"])
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# sample_copy = numbers.copy()
# print(sample_copy)
# sample_copy.append("vasu")
# print(sample_copy)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.clear()
# print(numbers)


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5,1,9,9,9]
# # print(numbers.count(1))
# print(numbers.index(9))


# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# print(numbers)
# obj = numbers.remove(1)
# print(obj)
# print(numbers)



# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# obj = numbers.pop(2)
# print(obj*5)
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.insert(2, "vasu kumar")      # Inserting 10 at index 2
# print(numbers)

# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.reverse()
# print(numbers)
# numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# numbers.sort(reverse=True)      
# print(numbers)


# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix[0][1])
# print(matrix[2][1])
# print(matrix[1][2])


#syntax
# [expression for item in iterable]
# empty_list = []
# for i in range(5):
#     result = i ** 2
#     empty_list.append(result)
# print(empty_list)

# [expression for item in iterable]
# result = [i**2 for i in range(5)]
# print(result)

# print([i**2 for i in range(5)])

# empty_list = []
# for i in range(10):
#     if i%2==0:
#         empty_list.append(i)
# print(empty_list)

# [exp for item in iterable if condition]
# result = [i for i in range(10) if i%2==0 ]
# print(result)


# print([i for i in range(10) if i%2==0 ])



# emp_details = ["charisma","vasu","sreenu","sreenu","srinivas","srinivas","kiran","kiran","kiran","raju","raju","raju","sreenu","sreenu"]
# empty_list = []
# for i in emp_details:
#     if i!="sreenu":
#         empty_list.append(i)
# print(empty_list)


# result = [i for i in emp_details if i!="sreenu"]
# print(result)



# emp_details = ["charisma","vasu","sreenu","sreenu","srinivas","srinivas","kiran","kiran","kiran","raju","raju","raju","sreenu","sreenu"]
# print(len(emp_details))
















