def calculation(credit, percent, period, anuit): # Программа для расчета аннуитетного платежа
    forbank = credit * (percent / 100)
    forcredit = anuit - forbank
    print('Перидод :', period)
    print('Остаток долга на начало периода:', credit)
    print('Выплачено процентов', forbank)
    print('Выплачено тела кредита: ', forcredit)
    return forcredit


def anuity(percent, credit, n):
    i = percent / 100
    K = (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    A = round(credit * K, 2)
    return A


credit = float(input('Введите сумму кредита: '))
years = n = int(input('На сколько лет?: '))
percent = float(input('Сколько % годовых: '))

anuit = anuity(percent, credit, years)

period = 0
while period < years:
    period += 1
    if period != 4:
        print()
        credit -= calculation(credit, percent, period, anuit)
    else:
        print('Остаток долга: ', credit, '\n')
        years += int(input('На сколько продлить договор? '))
        n = years - 3
        percent = float(input('увеличение ставки до '))
        anuit = anuity(percent, credit, n)
        credit -= calculation(credit, percent, period, anuit)

else:
    print('Остаток долга: ', credit)