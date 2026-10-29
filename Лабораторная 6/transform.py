data = input('Введите целые числа:')
if not data.strip():
    numbers = []
else:
    numbers = [int(x) for x in data.split()]
new_numbers = [abs(x) for x in numbers]

print(f'Исходный список: {numbers}')
print(f'Новый список: {new_numbers}')