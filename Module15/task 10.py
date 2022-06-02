N = int(input('кол-во чисел: '))
sort = []

index = -1
for _ in range(N):
    sort.append(int(input('Введите число: ')))

print('До сортировки: ', sort)

for _ in sort:                  # бубле сорт
    index = -1
    while index < N - 2:
            index += 1
            if sort[index] > sort[index+1]:
                sort[index], sort[index+1] = sort[index+1], sort[index]

print('После сортировки: ', sort)

