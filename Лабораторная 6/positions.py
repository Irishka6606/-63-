data = input('Введите целые числа:')
if not data.strip():
    print('Нет данных')
else:
    numbers = [int(x) for x in data.split()]
    max_val = max(numbers)
max_indices = [index for index, value in enumerate(numbers) if value == max_val]

print(f'Индексы максимума: {max_indices}')