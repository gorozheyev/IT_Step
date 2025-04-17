# наибольший общий делитель двох чисел
# def common_divisor(a:int, b:int )->int:
#     if b == 0:
#         return a
#     else:
#         return common_divisor(b, a%b)
#
# a = 24
# b = 12
# print(f"НОД чисел {a} і {b} = {common_divisor(a, b)}")

# сумма чисел из заданного числа
# def sum_from_value(n:int):
#     if n == 0:
#         return 0
#     else:
#         return n%10 + sum_from_value(n//10)
#
# amount = 123
# print(f'amount from {amount} = {sum_from_value(amount)}')

# проверка списка на симметричность
# def is_symmetric(lst:list)->bool:
#     if len(lst) == 0:
#         return True
#     elif lst[0] == lst[-1]:
#         return is_symmetric(lst[1:-1])
#     else:
#         return False
#
# list_real =[1,2,3,4,5,4,3,2,1]
# if is_symmetric(list_real):
#     print(f'list is symmetrical - {is_symmetric(list_real)}')
# else:
#     print(f'is not symmetrical - {is_symmetric(list_real)}')



