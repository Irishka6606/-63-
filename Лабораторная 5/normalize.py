text = input('Введите строку:')
old_length = len(text)

words = text.split()
normalized_text = ''.join(words)
new_length = len(normalized_text)

print(f'Исходная длина: {old_length}')
print(f'Новая длина: {new_length}')
print(f'Нормализованный текст: {normalized_text}')
print(f'Количество слов: {len(words)}')




