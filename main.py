from  constants import *

# print('Fist Pyton lesson')
# print('This is a test message')
# print('some text', 'second text', 2025, 'third text', sep='\n\t/')
#
#
# a= int(input('введите число: '))
# b= int(input('введите второе число: '))
#
# c = a*b
# print('произведение чисел ', a , '*', b, '=', c,  type(a))
# print('это число ПИ ', PI)

# first = int(PI//1)
# second = int(PI*10%10)
# third = int(PI*100)%10
# result = (first + second + third )**3
# print('сумма чисел PI в степени 3; ', result)
#
# dollar = 41.4
# valuta_usa = float(input('введите сумму в долларах: '))
# valuta_ua = dollar*valuta_usa
# print(int(valuta_ua), 'грн', int(round(((valuta_ua -valuta_ua//1)*100), 0)), 'копеек')

value1 = float(input('введите первое число: '))
value2 = float(input('введите второе число: '))
summ = int(value1+value2)
bool_value = not bool(summ%3)
print('сумма двух чисел кратна 3 ', bool_value)