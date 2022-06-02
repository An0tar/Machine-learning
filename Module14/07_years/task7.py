def same_num(num):
    flag = False
    for i in range(0,10):
        check = 0
        for sym in str(num):
            if i == int(sym):
                check += 1
            if check >= 3:
                flag = True
    return flag

first_year = int(input('Введите год отсчета:'))
last_year = int(input('Введите конечный год:'))
print('Года в промежутке с 3 одинаковыми цифрами')
for year in range(first_year, last_year + 1):
    if same_num(year):
        print(year)
