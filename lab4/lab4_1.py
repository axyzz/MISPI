def isCorrect(inp):
    summ = 0
    for num in inp[:-1]:
        summ += int(num)
    if summ % 2 == int(inp[-1]):
        return True
    else:
        return False

def createError(inp):
    if inp[0] == '0': inp = '1' + inp[1:]
    else: inp = '0' + inp[1:]
    return inp

msg = input('Введите двоичное кодовое слово: ')
summ = 0
for num in msg:
    summ += int(num)
msg += str(summ % 2)
print('Исходное слово: ', msg[:-1])
print('Слово с проверочным разрядом: ', msg)
print('Проверка на корректность сообщения: ', isCorrect(msg))
msg = createError(msg)
print('Добавим ошибку в первый разряд. Сообщение: ', msg)
print('Теперь проверка на корректность: ', isCorrect(msg))

