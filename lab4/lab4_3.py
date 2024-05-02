# вариант 2: N кратно 3

from random import randint

# исходное сообщение
N = '100110111'
"""
100
110
111
"""

# прямоугольный код представим в виде строки
def coder(msg):
    output = ''
    for i in range(0, len(N), 3):
        output += msg[i:i+3]
        output += str((int(msg[i]) + int(msg[i+1]) + int(msg[i+2])) % 2)
    for i in range(4):
        summ = 0
        for j in range(len(output) // 4):
            summ += int(output[i + j*4])
        output += str(summ % 2)
    return output

def createErrors(n, msg):
    for i in range(n):
        pos = randint(0, len(msg)-1)
        if msg[pos] == '0': msg = msg[:pos] + '1' + msg[pos+1:]
        else: msg = msg[:pos] + '0' + msg[pos+1:]
        print('Создана ошибка на позиции ', pos)
    print('Создано ', n, ' ошибок')
    return msg

def findErrors(msg):
    incor_row = []
    incor_col = []
    for i in range(0, len(msg), 4):
        if (int(msg[i]) + int(msg[i+1]) + int(msg[i+2])) % 2 != int(msg[i+3]): incor_row.append(i//4)
    for i in range(4):
        summ = 0
        for j in range((len(msg) // 4) - 1):
            summ += int(msg[i + j*4])
        if summ % 2 != int(msg[-4+i]): incor_col.append(i)
    return incor_row, incor_col

def fixError(msg, pos):
    if msg[pos] == '0': msg = msg[:pos] + '1' + msg[pos+1:]
    else: msg = msg[:pos] + '0' + msg[pos+1:]
    print('Исрпавлена ошибка на позиции ', pos)
    return msg

print('Исходное сообщение: ', N)
N_coded = coder(N)
print('Закодированное сообщение: ', N_coded)
errors = int(input('Количество ошибок: '))
N_error = createErrors(errors, N_coded)
print(N_error)
rows, cols = findErrors(N_error)
if len(rows) == len(cols) == 1:
    print('Была обнаружена ошибка в ', rows[0]+1, ' ряду в ', cols[0]+1, ' столбце')
    N_fixed = fixError(N_error, rows[0]*4 + cols[0])
    print('Исправленное сообщение: ', N_fixed)
else:
    print('Были обнаружены две или более ошибок')
