# 2-Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# input_data = input("Введите элементы списка из целых чисел через пробел: ")
# original_list = input_data.split(",")

# if len(original_list)%2 == 0:
#     lenght_list = len(original_list)//2
# else:
#     lenght_list = len(original_list) // 2 + 1

# for index in range(lenght_list):
#     print(int(original_list[index])*int(original_list[len(original_list) - 1 - index]))
input_data = input("Введите элементы списка из целых чисел через пробел: ")
original_list = input_data.split(" ")

if len(original_list)%2 == 0:
    lenght_list = len(original_list)//2
else:
    lenght_list = len(original_list) // 2 + 1

for index in range(lenght_list):
    print(int(original_list[index])*int(original_list[len(original_list) - 1 - index]))