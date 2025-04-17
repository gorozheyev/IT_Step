value = int(input('enter a size of squear: '))
for i in range(10):
    for j in range(10):
        if (j+i)%2 == 0:
            for k in range(value):
                print('x' , end=' ')
        else:
            for m in range(value):
                print('o', end=' ')
    print()



# for k in range(value):
#     print('x'*value)
