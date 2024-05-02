# вариант 2
# составить программу которая выводит смежный класс и лидеров смежного класса
# кодовый класс задается в коде программы. некодовое слово вводится в программу.

codewords = ([0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 1], [1, 1, 0, 1])
print('Кодовые слова: ', codewords)
wrong = tuple(map(int, input('Введите не кодовое слово: ').split(' ')))

wrongwords = []
for word in codewords:
    res = []
    for i in range(len(word)):
        res.append(word[i] ^ wrong[i])
    wrongwords.append(res)

leaders = []
cnt = len(wrong)
for word in wrongwords:
    temp = 0
    for elem in word:
        temp += elem
    if temp < cnt: cnt = temp

for word in wrongwords:
    temp = 0
    for elem in word:
        temp += elem
    if temp == cnt: leaders.append(word)

print('Смежный класс: ', wrongwords)
print('Лидер(ы): ', leaders)
