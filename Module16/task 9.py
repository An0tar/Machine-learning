friends = int(input('Сколько друзей? '))
papers = int(input('Сколько расписок? '))

cred = []

for i in range(1, 1 + friends):
    cred.append([i, 0])

for i in range(papers):
    print(i + 1 ,' расписка')
    whom = int(input('кому: '))
    who = int(input('от кого: '))
    money = int(input('Сколько: '))
    for index in cred:
        if index[0] == whom:
            index[1] += money
        if index[0] == who:
            index[1] -= money

for index in cred:
    for i in index:
        print(i,end = ':')
    print()