# Задание 1.б
# Вариант 16(2)
# Составить программу, которая выводит все кодовые слова и определяет кодовое расстояние

# порождающая матрица
# по определению комбинация строк - базис 
G = [[1, 1, 1, 0, 1, 0, 0, 0],
     [0, 1, 0, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 0, 1, 0, 1],
     [1, 0, 0, 1, 1, 0, 1, 0]]

codewords = []
# проход
for i in range(3):
    for j in range(i+1,4):
        word = ''
        for k in range(8):
            word += str(G[i][k] ^ G[j][k])
        codewords.append(word)
for i in range(4):
    codewords.append(''.join(map(str,G[i])))
word = ''
for k in range(8):
    word += str(G[0][k] ^ G[1][k] ^ G[2][k])
codewords.append(word)
word = ''
for k in range(8):
    word += str(G[0][k] ^ G[2][k] ^ G[3][k])
codewords.append(word)
word = ''
for k in range(8):
    word += str(G[0][k] ^ G[1][k] ^ G[3][k])
codewords.append(word)
word = ''
for k in range(8):
    word += str(G[1][k] ^ G[2][k] ^ G[3][k])
codewords.append(word)

codewords = list(sorted(set(codewords)))
print('Порождающая матрица: ')
for row in G:
    print(row)
print('Полученные кодовые слова: ')
for word in codewords:
    print(word)

differences = []
for i in range(len(codewords)-1):
    for j in range(i+1, len(codewords)):
        differences.append(sum(codewords[i][k] != codewords[j][k] for k in range(len(codewords[i]))))
print('Кодовое расстояние: ', min(differences))
