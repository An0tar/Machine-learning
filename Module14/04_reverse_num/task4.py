def reverse(text):
    flag = False
    check = -1
    whole = ''
    fraction = ''
    for sym in text:
        if sym != '.' and not(flag):
            whole = sym + whole
        else:
            flag = True
        if flag:
            fraction = sym + fraction
            check += 1
    if flag:
        sum = float(whole + fraction) / (10**check)
    else:
        sum = whole
    return sum

N = (input('Введите первое число: '))
K = (input('Введите второе число: '))

print('Первое число наоборот: ',reverse(N))
print('Второе число наоборот: ',reverse(K))
print('Сумма:', reverse(K) + reverse(N))