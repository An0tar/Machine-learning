number = int(input('Введите число: '))
min = number
for num in range(number, 1, -1):
    if number % num == 0:
        min = num
print('Наименьший делитель, отличный от единицы:', min)