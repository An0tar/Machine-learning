def bye(count, number, index):
    index -= 1
    for _ in range(number):
        index += 1
    index %= count
    return index



people_count = int(input('Кол-во человек:'))
number = int(input('Какое число в считалке? '))
print('Каждый ', number, ' человек выбывает')

people = list(range(1, people_count + 1))
last_index = 0

while len(people) > 1:
    print('Текущий круг людей: ', people)
    if len(people) <= last_index:
        last_index -= 1
        print('Начала отсчета с ', people[0])
        last_index = 0
    else:
        print('Начала отсчета с ', people[last_index])
    last_index = bye(len(people), number, last_index)
    leaver = people.pop(last_index)
    print('Уходит человек №', leaver)


print('Остался №: ', people[0])