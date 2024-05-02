"""Составить программу, которая кодирует строку любой длины,
составляет кодовый словарь и выводит закодированное сообщение."""

from numpy import log2
from math import ceil

source = input("Введите строку:")
letters = set(source)
bits = ceil(log2(len(letters)))

coder = {}
n = 0
for letter in letters:
    coder[letter] = f"{bin(n)[2:]:0>{bits}}"
    n+=1

coded = ""
for letter in source:
    coded += coder[letter]

print("Исходная строка: ", source, "\nКодовый словарь: ", coder, "\nЗашифрованная строка: ", coded)
