rolls_count = int(input('Сколько роликов: '))
rolls = []

for i in range(rolls_count):
    print('Размер ', i + 1, ' коньков', end = ':')
    rolls.append(int(input()))

people_count = int(input('Сколько людей: '))
people = []

for i in range(people_count):
    print('Размер ноги', i + 1, ' человека', end = ':')
    people.append(int(input()))

check = 0

for size in people:
    if rolls.count(size) > 0:
        rolls.remove(size)
        check += 1

print('Наибольшее кол-во людей, которые могут взять ролики:', check)
