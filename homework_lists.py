from random import randint

list1= []
list2 =[]
length = int(input('enter a list length: '))

for i in range(length):
    list1.append(randint(-10,10))
print('first list -', list1)

for j in range(length):
    list2.append(randint(-10, 10))
print('second list -',list2)

list3 = list1 + list2
print('commont list1 + list2\n',list3)

list4 =[]
for i in list3:
    if i not in list4:
        list4.append(i)
print('unique values from both lists\n', list4)

list5 = []
for i in list1:
        if i in list2:
            list5.append(i)
            continue
print('common elements from both lists without duplicates\n' ,list5)

list6 =[]
list7 = []
for i in list1:
    if i not in list6:
        list6.append(i)
for i in list2:
    if i not in list7:
        list7.append(i)
list6.extend(list7)
print('unique values for each lis\n', list6)

list8 = []
list8.append(max(list1))
list8.append((min(list1)))
list8.append(max(list2))
list8.append(min(list2))
print('list from max and min values from each list\n', list8)