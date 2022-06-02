def symmetry(lst):
    reverse_list = []
    for i in range(len(lst) - 1, -1, -1):
        reverse_list.append(lst[i])
    if lst == reverse_list:
        return True
    else:
        return False

N = int(input('Скоьлко чисел: '))
num = []
new = []
final = []
for _ in range(N):
    num.append(int(input('Введите число: ')))

for i_num in range(0, len(num)):
    for j_num in range(i_num, len(num)):
        new.append(num[j_num])
    if symmetry(new):
        for i_final in range(0, i_num):
            final.append(num[i_final])
        final.reverse()
        break
    new = []

print('Исходный список: ', num)
print('Нужно чисел:', len(final))
print('Список чисел: ', final)