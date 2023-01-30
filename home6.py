import random

# Задача 1. Дано натуральное число N. Найдите значение выражения:N + NN + NNN
# N может быть любой длины. N = 132:132 + 132132 + 132132132 = 132264396
def zadacha1():
    number = input('Введите число: ')
    new_number1= number + number
    new_number2 = number + new_number1
    result = int(number) + int(new_number1) + int(new_number2)
    print(f'{number} + {new_number1} + {new_number2} = {result}')
 

# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет
def zadacha2():
    numbers = [str(random.randint(1,9)) for _ in range(15)]
    print(numbers)
    user_number = int(input('Введите 3-значное чило: '))
    result =''.join(numbers)
    print(result)    

    if str(user_number) in result:
        print(' Yes')
    else:
        print('No') 

# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.
from fractions import Fraction
def check_numbers(x,y):
    min_numbers = min(x,y)
    nod = 1
    for el in range(2,min_numbers+1):
        if x % el == 0 and y % el == 0:
            nod = el
            break
    return nod == 1    

def zadacha3():
    for y in range (1,12):
        for x in range(1,y):
            if check_numbers(x,y):
                print(f'{x}/{y}', end=' ')
        print()



# zadacha1() 
# zadacha2()
zadacha3()