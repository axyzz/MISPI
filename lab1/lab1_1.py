"""Составить программу для определения какое количество информации несет сообщение о том, 
что горит красный и желтый сигнал светофора, среднее количество информации о том, 
что загорелся любой из трех сигналов"""

from numpy import log2

red = 108
yellow = 4
green = 16

lights = {"red" : red, "yellow" : yellow, "green" : green}
cycle = sum(lights.values())

ry_prob = (lights["red"] + lights["yellow"]) / cycle
ry_info = log2(1 / ry_prob)

avg_info = 0
for color in lights:
    prob = lights[color]/cycle
    avg_info += prob * log2(1 / prob)

print("Информация из красного и желтого: ", ry_info, "\nСреднее количество информации: ", avg_info)
