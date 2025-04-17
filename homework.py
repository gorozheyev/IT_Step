# digit = input('введите первое число из четырех цифр: ')
# reverse = digit[::-1]
# print('число выеденное наоборот: ', int(reverse))

# min_value = 1
# max_value = 12
# season = ''
# bool_value = False
# value = int(input('введите номер месяца года: '))
# if value >= min_value and value <= max_value:
#     bool_value =True
#     if value >=3 and value <=5:
#         season = 'Spring'
#     elif value >=6 and value <=8:
#         season = 'Summer'
#     elif value >=9 and value <=11:
#         season = 'Otemn'
#     else:
#         season = 'Winter'
# if  bool_value:
#         print( 'this is',  season)
# else:
#     print('введенное значение не корректно')

# --------------------------------------

number = input('please enter six digit number: ')
sum1 = 0
sum2 = 0
if number.isdigit() and len(number) ==6:
    for x in number[:3]:
        sum1 = sum1+int(x)
    for y in number[3:]:
        sum2 = sum2 + int(y)
    if sum1 == sum2:
        print('this is lucky digit')
else:
    print('the number is not 6 digit')
