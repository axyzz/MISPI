# 2 вариант 
# создать программу для для кодирования методом хэмминга двоичного слова (7,4) 
# и определения номера искаженного разряда
from random import randint

inp = '0010'

def coder(src):
    # out = x1 + x2 + inp[0] + x4 + inp[1] + inp[2] + inp[3] 
    out = ''
    out += str((int(inp[0]) + int(inp[1]) + int(inp[3])) % 2)
    out += str((int(inp[0]) + int(inp[2]) + int(inp[3])) % 2)
    out += inp[0]
    out += str((int(inp[0]) + int(inp[2]) + int(inp[3])) % 2)
    for i in range(1,4):
        out += inp[i]
    return out

def makeError(src):
    index = randint(0,7)
    src = src[:index] + str(int(not(int(src[index])))) + src[index+1:]
    return src

def findError(src):
    s1 = (int(src[3]) + int(src[4]) + int(src[5]) + int(src[6])) % 2
    s2 = (int(src[1]) + int(src[2]) + int(src[5]) + int(src[6])) % 2
    s3 = (int(src[0]) + int(src[2]) + int(src[4]) + int(src[6])) % 2
    s = str(s1) + str(s2) + str(s3)
    return int(s, 2)

print('Исходное слово: ', inp)
inp_coded = coder(inp)
print('Закодированное слово: ', inp_coded)
inp_error = makeError(inp_coded)
print('Слово с ошибкой: ', inp_error)
i_error = findError(inp_error)
print('Ошибка обнаружена в ', i_error, ' разряде')
