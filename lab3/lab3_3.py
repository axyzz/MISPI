# словарь для кодирования и декодирования
code = {'a' : '0', 'b' : '10', 'c' : '1100', 'd' : '1101', 'e' : '1110', 'f' : '11110', 'g' : '11111'}

def coder(inp):
    output = ''
    # кодирование каждого символа
    for char in inp:
        output += code[char]
    return output

def decoder(inp):
    temp = ''
    output = ''
    i = 0
    while i < len(inp):
        # ищем подстроки равные кодовым словам
        temp += inp[i]
        if temp in code.values():
            # получаем индекс нужного нам значения в словаре
            # образаемся к ключу по этому индексу
            output += list(code.keys())[list(code.values()).index(temp)]
            temp = ''
        i += 1
    return output

word = input('Введите слово для кодировки - декодировки: ')
encrypted = coder(word)
decrypted = decoder(encrypted)

print('Закодированное слово: ', encrypted)
print('Декодированное слово: ', decrypted)
