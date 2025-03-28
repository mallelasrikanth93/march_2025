# single_quoted_string = 'Hello, World!'
# double_quoted_string = "Python Strings  8 O'clock"
# print(double_quoted_string)
# triple_quoted_string = '''Triple quotes allow he said, " triple" 8 O'clock
# strings to span multiple lines.'''
# print(triple_quoted_string)
# print(type(single_quoted_string))
# print(type(double_quoted_string))
# print(type(triple_quoted_string))


# my_string = "Python life"
# print(my_string[0]) #P
# print(my_string[7]) #l
# print(my_string[10]) #e


# my_string = "Python life"
# print(my_string[-1])#e
# print(my_string[-7])#o



# my_string = "Python life"
# print(my_string[7:])
# print(my_string[-4:])
#seq[s:s:s]
# print(my_string[1:6])
# print(my_string[::])
# print(my_string[-10:-5])
# print(my_string[::-1])
# print(my_string[11:6:-1])
# print(my_string[-1:-5:-1])


# my_string = "Python life"
# print(id(my_string))
# uc = my_string.upper()
# print(id(uc))
# print(uc)
# print(my_string)


# sample = "welcome to PYTHONLIFE @8 O'Clock"
# print(sample)
# uc=sample.upper()
# print(uc)


# sample = "welcome to PYTHONLIFE @8 O'Clock"
# print(sample)
# lc=sample.lower()
# print(lc)


# sentence = "This is a sample sentence."
# count_i = sentence.count('sample sentence')
# print(count_i) 


# whitespace_string = "   This is a string with leading and trailing whitespace.   "
# print(len(whitespace_string))
# stripped_string = whitespace_string.strip()
# print(len(stripped_string))
# print(stripped_string)


# data = "Pythonlife,Kiran,123456"
# data1 = data.split(',')
# print(data1)

# original_string = "Python is fun!  fun fun fun fun"
# modified_string = original_string.replace('fun', 'awesome')

# print(modified_string)


# filename = "example.txt"
# starts_with = filename.startswith("ex")
# ends_with = filename.endswith(".txt")
# print(starts_with)  
# print(ends_with) 



# email_list = ["example1@gmail.com", "example2@yahoo.com", "example3@gmail.com", "example4@hotmail.com","example5@outlook.com"]
# empty_list = []
# for i in email_list:
#     if i.endswith("@gmail.com"):
#         empty_list.append(i)
# print(empty_list)

# # [exp for i in iter if cond]
# result = [i for i in email_list if i.endswith("@gmail.com")]
# print(result)
# print([i for i in email_list if i.endswith("@gmail.com")])



# sentence = "This is a sentence."
# position_a = sentence.find('z')
# position_i = sentence.index('z')
# print(position_a)
# print(position_i) 


# text = "python programming"
# capitalized_text = text.capitalize()
# print(capitalized_text)

# sample = "welcome to pythonlife"

# isdigit(): Returns True if all characters in the string are digits.
# isalpha(): Returns True if all characters in the string are alphabetic.
# numeric_string = "12345"
# alpha_string = "Python1234"
# is_numeric = numeric_string.isdigit()
# is_alpha = alpha_string.isalpha()
# print(is_numeric)  
# print(is_alpha)  

# word_list = ['Hello', 'World']
# joined_string = ' '.join(word_list)

# print(joined_string)











emp_details = ["charishma","vasu","sreenu","sreenu","srinivas","kiran","kiran","sreenu","kiran","charishma","vasu","srinivas"]
print(emp_details[0])
sreenu_index = []
for i in range(len(emp_details)):
    if emp_details[i] == "sreenu":
        sreenu_index.append(i)
print(sreenu_index)
print([i for i in range(len(emp_details)) if emp_details[i] == "sreenu"] )

result = [len(word) for word in emp_details]
print(result)