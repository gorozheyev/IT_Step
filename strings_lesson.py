from random import randint
# for i in range(3):
#     value = input('enter a value: ')
#     if value.isdigit():
#         print('value can be formated to INT =', int(value))
#         break
#     elif value.count('.') > 1:
#         print('value can be formated to INT =', int(value.replace('.', '')))
#         break
#     elif value.count(',') > 1:
#         print('value can be formated to INT =', int(value.replace(',', '')))
#         break
# print('program finished')
#
# ---------------------------
# count_of_persons = int(input('enter count of students: '))
# person_data =[]

# for i in range(count_of_persons):
#     name_surname = input('enter your Name and Surname: ')
#     age = int(input('enter your Age: '))
#     present = input('enter value Yae or No , present peson:')
#     height = float(input('enter your Height in format 0.0:'))
#     group_name = input('enter your Group name:')
#     person_data.append([name_surname, age, present, height, group_name])
# print(person_data)

list =[]
new_list =[]
sum = 0
length = int(input('enter the length of list:'))
start_value = int(input('enter start value: '))
end_value =int(input('enter end value: '))
for i in range(length):
    list.append(randint(start_value, end_value))
print(list)
for j in list:
    sum= sum+j
print(round(sum/length, 3))

for i in list:
    if i in list:
        list.remove(i)
print(list)