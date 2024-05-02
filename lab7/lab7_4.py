# составить программу которая будет определять четность подстановки порядка n

inp = [1, 4, 3, 2, 6, 5]
cnt = 0

for i in range(len(inp) - 1):
    for j in range(i + 1, len(inp)):
        if inp[j] < inp[i]: cnt += 1

print('Исходная подстановка: ', inp)
print('Количество инверсий: ', cnt)
if cnt % 2 == 0:
    print('Подстановка четная')
else:
    print('Подстановка нечетная')
