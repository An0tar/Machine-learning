# Дано целое число N. Напишите программу, которая формирует список из нечётных чисел от 1 до N.

N = int(input('Введите число: '))

num_list = []

for num in range(1, N+1):
    if num % 2 == 1:
        num_list.append(num)

print(num_list)