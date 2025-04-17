# сумма из диапазона
from itertools import count


def sum_from_range(a: int, b:int):
    c = 0
    summa = 0
    list = []
    if a > b:
        c = a
        a = b
        b = c
    while b >= a:
        list.append(a)
        a+=1
    return sum(list)

sum_values = sum_from_range(9,3)
print(sum_values)

# произведение значений из списка
def multy_from_list(list):
    multy = 1
    if len(list) < 2:
        return 0
    else:
        for i in list:
            multy = multy*i
    return multy

new_list = [-3,-4,3,7,13,17,5,3,11]
print(multy_from_list(new_list))

# миниамльное значение из списка
def min_from_list(list):
    if len(list) < 2:
        return 0
    else:
        return min(list)

print(min_from_list(new_list))

# каунт простых чисел из списка
def simple_values_from_list(list):
    count = 0
    for i in list:
        if i > 1:
            for j in range(2,i):
                if j % i == 0:
                    break
            count = count +1
    return count

print(simple_values_from_list(new_list))

def del_value_from_list(list, value: int):
    count =0
    if len(list) < 2:
        return 0
    else:
        for i in list:
            if i == value:
                list.remove(i)
                count = count +1
    return count

print(del_value_from_list(new_list, 3))

# возвращает общий список
def common_list(list1, list2):
    if len(list1) < 2 or len(list2) <2:
        return 0
    return list1 + list2

list_1 = [-3,-4,3,7,13,17,5,3,11]
list_2 = [2,5,7]
print(common_list(list_1, list_2))

def power_new_list(list, a):
    list_pow =[]
    if len(list) < 2:
        return 0
    else:
        for i in list:
            list_pow.append(i**a)
    return list_pow

print(power_new_list(list_2, 2))

