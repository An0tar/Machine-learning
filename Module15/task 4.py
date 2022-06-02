# В базе одного магазина электроники есть список видеокарт компании NVIDIA разных поколений.
# Для удобства в списке вместо полных названий хранятся только числа,
# они обозначают модель и поколение видеокарты. Недавно компания выпустила новую линейку видеокарт,
# и в итоге самые старшие поколения разобрали за пару дней.
#
# Напишите программу, которая удаляет из этого списка видеокарт наибольшие элементы.

count = int(input('Кол-во видеокарт: '))
videocard = []

for i in range(count):
    print(i+1, 'Видеокарта: ', end = '')
    model = int(input())
    videocard.append(model)

print('Старый список: ', videocard)

max = max(videocard)

new_list = []
index = -1

for model in videocard:
    index += 1
    if videocard[index] != max:
        new_list.append(videocard[index])

print('Новый список видеокарт:', new_list)

