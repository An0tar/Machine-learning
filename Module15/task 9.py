word = list(input('Введите слово: '))
if word == word[::-1]:
    print('Да, является')
else:
    print('Нет, не является')