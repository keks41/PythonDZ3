# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#  - [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
input_data = input("Введите элементы списка из вещественных чисел: ")
original_list = input_data.replace(" ", "").split(",")

fractal_list = []

for element in original_list:
    fractal_element = str(float(element)).split(".")
    print (fractal_element)
    if fractal_element[1] != '0':
        fractal_list.append(fractal_element[1])

total_frac_list = []
for index in range(len(fractal_list)):
    fractal_list[index] = "0." + fractal_list[index]


min_value = float(fractal_list[0])
max_value = float(fractal_list[0])


for element in fractal_list:
    if float(element) > float(max_value): max_value = float(element)
    if float(element) < float(min_value): min_value = float(element)

print(f"Разница между минимальной и максимальной дробной частью элементов равна {max_value - min_value}")