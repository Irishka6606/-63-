n = int(input('Введите n:'))
count = 0
sum = 0

for _ in range(n):
    num = int(input('Введите число:'))
    if num % 2 == 0:
        count = count + 1
        sum = sum + num

print('Количество:', count)
print('Сумма:', sum)