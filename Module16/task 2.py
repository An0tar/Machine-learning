first_class = list(range(160, 177, 2))
second_class = list(range(162, 181, 3))
union = []
union.extend(first_class)
union.extend(second_class)
union.sort()

print('Получившаяся шеренга: ', union)