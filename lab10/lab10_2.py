# умножение полиномов 
def mult(x, y):
    n1 = len(x)
    n2 = len(y)
    prod = [0] * (n1 + n2 - 1)

    for i in range(n1):
        for j in range(n2):
            prod[i + j] ^= x[i] * y[j]
    return prod


g = [1, 1, 0, 0, 1]  # производящий полином
msgs = [[0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 0, 1, 1],
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 1, 0],
        [1, 1, 1, 1]]
        
print('Производящий полином g(x) = x^4 + x + 1')
print('Все кодовые слова:')
for msg in msgs:
    res = mult(msg, g)
    for c in msg:
        print(c, end='')
    print(' -> ', end='')
    for c in res:
        print(c, end='')
    print()
