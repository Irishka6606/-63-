from functions import sum_digits, average, normalize_text, select_numbers, is_palindrome

num = int(input('Введите целое число: '))
print('Сумма цифр:', sum_digits(num))

nums = list(map(int, input('Введите числа через пробел: ').split()))
avg = average(nums)
print('Среднее:', avg if avg is not None else 'Нет данных')

text = input('Введите текст: ')
print('Текст:', normalize_text(text))

threshold = int(input('Введите порог: '))
print('Результат:', select_numbers(nums, threshold))

pal_text = input('Введите текст для проверки на палиндром: ')
print('Это палиндром?', is_palindrome(pal_text))