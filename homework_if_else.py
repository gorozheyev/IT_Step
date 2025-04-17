value = int(input('enter a valur from 1 to 100: '))
if  value >= 1  and value <= 100:
    if value % 3 == 0 and value % 5 == 0:
        print('Fizz Buzz')
    elif  value%5 == 0 and value >=5:
        print('Buzz')
    elif  value%3 == 0 and value >= 3:
        print('Fizz')
    elif value%3 !=0 or value%5 !=0:
        print(value)
else:
    print('entered value is noy in range')

# --------------------------

value1 = float(input('введите продажи первого менеджера: '))
value2 = int(input('введите продажи второго менеджера: '))
value3 = float(input('введите продажи третьего менеджера: '))
salary = 200
salary1=0
salary2=0
salary3=0

if value1 < 500:
    salary1 = salary + value1*0.03
    print(salary1)
elif value1 >= 500 and value1 <=1000:
    salary1 = salary + value1 * 0.05
    print(salary1)
else:
    salary1 = salary + value1 * 0.08
    print(salary1)

if value2 < 500:
    salary2 = salary + value2*0.03
    print(salary2)
elif value2 >= 500 and value2 <=1000:
    salary2 = salary + value2 * 0.05
    print(salary2)
else:
    salary2 = salary + value2* 0.08
    print(salary2)

if value3 < 500:
    salary3 = salary + value3 * 0.03
    print(salary3)
elif value3 >= 500 and value3 <= 1000:
    salary3 = salary + value3 * 0.05
    print(salary3)
else:
    salary3 = salary + value3 * 0.08
    print(salary3)

if salary1 > salary2 and salary1 > salary3:
    print(salary1,  salary2)
    print(salary1 > salary2)
    print('лучший менеджер №1, зп с пермийей = ', salary1 + 200)
if salary2 > salary1 and salary2 > salary3:
    print('лучший менеджер №2, зп с пермийей = ', salary2 + 200)
if salary3 > salary1 and salary3 > salary2:
    print('лучший менеджер №3, зп с пермийей = ', salary3 + 200)

