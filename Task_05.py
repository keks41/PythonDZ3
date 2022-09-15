# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи](https://clck.ru/yWbkX.)
def fiboPositive(n):
    listFib01 = [0, 1]
    for i in range(2, n + 1):
        listFib01.append(listFib01[i - 2] + listFib01[i - 1])
    return listFib01

def fiboNegative(n):
    listFib02 = [0, 1]
    for i in range(2, n + 1):
        listFib02.append(listFib02[i - 2] - listFib02[i - 1])
        listFib03 = listFib02[1::]
    listFib03.reverse()
    return listFib03

n = 8
fiboPos = fiboPositive(n)
fiboNeg = fiboNegative(n)
resFibo = fiboNeg + fiboPos
print(f"Список чисел Фибоначчи c отрицательными и положительными индексами: \n{resFibo}")