# Дан список из N элементов и целое число K.
# Напишите программу, которая циклически сдвигает элементы списка вправо на K позиций.
# Используйте минимально возможное количество операций присваивания.

N = int(input('Кол-во элементов: '))
tablo = []

for _ in range(N):
    tablo.append(input('Введите элемент: '))

K = int(input('На сколько сдвинуть? '))
print('Изначальный список:', tablo)

for _ in range(K):
    new_tablo = []
    index = -2
    for _ in tablo:
        index += 1
        new_tablo.append(tablo[index])
    tablo = new_tablo

print('Сдвиг:', K, tablo)
