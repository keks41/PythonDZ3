# ; 1- Задайте список из нескольких чисел. Напишите программу,
# ; которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# ; *Пример:*

# ; - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

input_number = input("Введите целые числа через пробел :")
 
enter_list = input_number.split(" ")
sum = 0
for index in range(len(enter_list)):
    if index % 2 != 0:
        sum += int(enter_list[index])
print(f"Сумма чисел стоящих на нечетной позиции = {sum}")
