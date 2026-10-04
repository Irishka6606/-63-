order = input("Название заказа: ")
name = input("Имя заказчика: ")

name1 = input("Первая позиция: ")
qty1 = int(input("Количество: "))
price1 = float(input("Цена: "))

name2 = input("Вторая позиция: ")
qty2 = int(input("Количество: "))
price2 = float(input("Цена: "))

delivery = float(input("Доставка: "))
paid = float(input("Внесено: "))

sum1 = qty1 * price1
sum2 = qty2 * price2
total_items = sum1 + sum2
total = total_items + delivery
total_qty = qty1 + qty2
change = paid - total

print(f"\nЗаказ: {order}")
print(f"Заказчик: {name}")
print(f"{name1} | {qty1} | {price1:.2f} | {sum1:.2f}")
print(f"{name2} | {qty2} | {price2:.2f} | {sum2:.2f}")
print(f"Товары: {total_items:.2f}")
print(f"Итого: {total:.2f}")
print(f"Количество: {total_qty}")
print(f"Сдача: {change:.2f}")