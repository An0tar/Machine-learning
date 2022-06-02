def checking(name, lst):
    exist = lst.count(name)
    if exist > 0:
        return True
    else:
        return False

guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке ', len(guests), ' человек', guests)
    stage = input('Гость пришёл или ушёл?: ')
    if stage == 'пришёл':
        name = input('Имя гостя:')
        if len(guests) < 6:
            print('Привет', name)
            guests.append(name)
        else:
            print('Мест нет', name)
    elif stage == 'ушёл':
        name = input('Имя гостя:')
        if checking(name, guests):
            print('Пока ', name)
            guests.remove(name)
        else:
            print('Такого гостя не было')
    elif stage == 'Пора спать':
        break
    print()
print('Вечеринка закончилась, все легли спать')
