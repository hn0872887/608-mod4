# c = [-45, 6, 0, 72, 1543]
# print(c)
# print(f"value at index 0: {c[0]}")
# print(f"value at index 4: {c[4]}")
# print(f"len of list: {len(c)}")
# print(f'value of last element using index -1: {c[-1]}')
# #print(c[6])
# a = (c[0] + c[1] + c[2])
# print(f'adding first three items in list c: {a}')
# empty_list = []
# empty_list += range(1, 6)
# print(f"empty list: {empty_list}")
# concatenated_list = c + empty_list
# print(f"concatenatedconcatenated_list: {concatenated_list}")
# for item in range(len(concatenated_list)):
#     print(f'{item} : {concatenated_list[item]}')
# a = [1, 2, 3]
# b = [1, 2, 3, 3]
# c = [2, 1, 3]
# print(a == b)
# print(a == c)
# print(b == c)
# def cube_list(values):
#     for i in range(len(values)):
#         values[i] **=3


# value_question14 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# cube_list(value_question14)
# print(f"list of numbers after cubing every item in a list: {value_question14}")

student_tuple = ()
print(f"making empty tuple: {student_tuple}")

print(f"length of an empty tuple: {len(student_tuple)}")

student_tuple = "John", "Green", 3.3
print(f"a new tuple with 3 elements: {student_tuple}")

print(f"access tuple elements by index 0: {student_tuple[0]}")

student_tuple += (40, 50)
print(f'adding more items including 40 and 50 to tuple: {student_tuple}')

student_tuple = ("Amanda", [98, 85, 87])
print(f"new student tuple followed the instructions in 5.4: {student_tuple}")

first_name, grades = student_tuple
print(f"first name of student in tuple: {first_name}")
print(f"grades of student in tuple: {grades}")

numbers = [19, 3, 15, 7, 11]
print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8} Bar')
for index, value in enumerate(numbers):
    print(f'{index:>5}{value:>8} {"*" * value}')

numbers = list(range(1, 16))
print(f'numbers list in section 5.5: {numbers}')
print(f"using slices of the list to get even numbers: {numbers[1:len(numbers):2]}")
numbers[5:10] = [0] * len(numbers[5:10])
print(f'using slices to replace some values with 0: {numbers}')
numbers[5:] = []
print(f"using slices to keep only the first 5 values: {numbers}")
numbers[:] =[]
print(f'using slices to delete all values: {numbers}')

list_numbers_question22 = list(range(0, 10))
print(f"numbers list for question 22: {list_numbers_question22}")
del list_numbers_question22[-1]
print(f"list of numbers after using del statement to remove the last element: {list_numbers_question22}")
def modify_elements(items):
    for i in range(len(items)):
        items[i]*= 2

numbers = [10, 3, 7, 1, 9]
modify_elements(numbers)
print(f"question 23: passing a list to a function: {numbers}")
sorted_numbers = sorted(numbers)
print(f"question 24: using the sort function: {sorted_numbers}")
sorted_numbers.sort(reverse=True)
print(f"question 24: using reverse to sort in descending order: {sorted_numbers}")

foods = ['Cookies', 'pizza', 'Grapes', 'apples', 'steak', 'Bacon']
foods.sort()
print(f"question 26: sorting text: {foods}")

numbers = [3, -7, 1, 4, 2, -8, 5, 6]
print(f'question 27: create a list {numbers}')
print(f"the index of value of 5: {numbers.index(5)}")
#print(f"the index of value of 8 start slicing from index 3: {numbers.index(8, 3)}")
print(f"check if 6 in numbers: {6 in numbers}")
print(f"check if 6 not in numbers: {6 not in numbers}")

list2 = [item for item in range(1, 6)]
print(f'using list comprehension to create a list: {list2}')