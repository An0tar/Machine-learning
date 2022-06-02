first_list = []
second_list = []
new_list = []

for _ in range(3):
    first_list.append(int(input('Введите элемент в первый список: ')))

new_list = first_list

for _ in range(7):
    second_list.append(int(input('Введите элемент во второй список: ')))

first_list.extend(second_list)

for i in new_list:
    temp = first_list.count(i)
    for _ in range(temp - 1):
        first_list.remove(i)

print('Уникальный список: ', first_list)
