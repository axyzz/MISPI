# Вариант 16 (1)
# Написать программу для определения средней длины кодовых слов
code_base = {'00' : 0.4, '01' : 0.2, '10' : 0.2, '1100' : 0.05, '1101' : 0.05, '1110' : 0.05, '1111' : 0.05}

avg = 0
for msg in code_base:
    avg += code_base[msg] * len(msg)
print(avg)
