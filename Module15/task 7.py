count = int(input('Сколько контейнеров: '))
containers = []

for _ in range(count):
    mass = int(input('Вес контейнера: '))
    if mass > 200:
        print('Масса слишком большая')
        break
    else:
        containers.append(mass)

new = int(input('Вес нового контейнера: '))

if new > 200:
    print('Масса слишком большая')
else:
    index = -1
    for weight in containers:
        index += 1
        if weight < new:
            break
    if containers[index] > new:
        index += 1
    print('Новое место контейнера: ', index+1)
