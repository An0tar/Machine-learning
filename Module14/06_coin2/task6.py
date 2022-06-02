import math

x = float(input('Введите координату х монетки: '))
y = float(input('Введите координату у монетки: '))
radius = float(input('Введите радиус поиска: '))

hyp = math.sqrt(x ** 2 + y ** 2)  # Нахождение длины гиппотенузы
if radius > hyp:
    print('Монетка рядом')
else:
    print('Монетка далеко')

