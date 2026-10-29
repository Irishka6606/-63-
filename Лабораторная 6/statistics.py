data = input('Введите целые числа:')

if not data.strip():
    print('Нет данных')
else:
    numbers = [int(x) for x in data.split()]

count = len(numbers)
total_sum = sum(numbers)
minimum = min(numbers)
maximum = max(numbers)
average = total_sum / count

print(f'Количество: {count}')
print(f'Сумма: {total_sum}')
print(f'Минимум: {minimum}')
print(f'Максимум: {maximum}')
print(f'Среднее: {average:.2f}')