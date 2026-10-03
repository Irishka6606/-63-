total = int(input('Введите общий объем:'))
capaciti = int(input('Введите вместимость одной единицы:'))

quantity = total // capaciti
remains = total % capaciti
min = (total + capaciti - 1) // capaciti

print('Полностью заполненых единиц:', quantity)
print('Остаток:', remains)
print('Минимальное число единиц:', min)