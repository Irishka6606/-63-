data = input('Введите целые числа:')
if not data.strip():
    numbers = []
else:
    numbers = [int(x) for x in data.split()]
selected = [x for x in numbers if x % 2 == 0]

if not selected:
    print('Результат: []')
    print('Количество: 0')
    print('Сумма: 0')
    print('Сортированная копия: []')
else:
    print(f'Исходный порядок: {selected}')
    print(f'Количество: {len(selected)}')
    print(f'Сумма: {sum(selected)}')
    print(f'Сортированная копия: {sorted(selected)}')