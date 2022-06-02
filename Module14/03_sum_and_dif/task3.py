def number_sum(N):
    num_sum = 0
    while N > 0:
        num_sum += N % 10
        N //= 10
    return num_sum

def num_count(N):
    total = 0
    while N > 0:
        total += 1
        N //= 10
    return total

N = int(input('Введите число: '))

print('Сумма цифр: ', number_sum(N))
print('Кол-во цифр в числе: ', num_count(N))
print('Разность суммы и кол-ва цифр:',number_sum(N) + num_count(N))

