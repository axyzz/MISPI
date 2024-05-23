# вычисление НОД и коэффициентов xa + yb = nod(a, b)
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


# решение системы по модулю p
def solve(a11, a12, a21, a22, b1, b2, p):
    delta = (a11 * a22 - a12 * a21) % p

    try: 
        delta_inv = mod_inverse(delta, p)
    except:
        return -1

    x = (a22 * b1 - a12 * b2) * delta_inv % p
    y = (a11 * b2 - a21 * b1) * delta_inv % p
    return x, y


# начальные значения
a11 = 3
a12 = 2
a21 = 1
a22 = 4
b1 = 7
b2 = 8
p = 11

# решение и вывод
x, y = solve(a11, a12, a21, a22, b1, b2, p)
print(f'Исходная система:\n{a11}x + {a12}y = {b1}\n{a21}x + {a22}y = {b2}\np = {p}')
print(f'Решение: x = {x} y = {y}')
