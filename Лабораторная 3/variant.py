n = int(input('Введите число от 9 до 100:'))

if n < 0 or n > 100:
    print('Ошибка диапазона')
elif n <= 19:
    print('Низкий')
else:
    print('Высокий')