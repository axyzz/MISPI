# вычисление НОД и коэффициентов xa + yb = nod(a, b)
# (расширенный метод Евклида)
def extended_euler(a, b):
    # базовый случай
    if a == 0:
        return b, 0, 1
    nod, x1, y1 = extended_euler(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return nod, x, y


# обратное по модулю p
def mod_inverse(a, p):
    nod, x, y = extended_euler(a, p)
    if nod != 1:
        raise ValueError(f'Inverse does not exist for a = {a} and p = {p}')
    return x % p


# интерфейс
a = input('Введите а:')
p = input('Введите р:')

try:
    inverse = mod_inverse(a, p)
    print(f'Обратный элемент к {a} по модулю {p} равен {inverse}')
except:
    print('Невозможно взять обратный элемент к {a} по модулю {p}')

