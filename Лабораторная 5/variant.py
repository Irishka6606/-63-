text = input('Введите строку:')
words = text.split()
suitable_words = []

for word in words:
    cleaned_word = word.strip('.,!?;:').lower()
    if not cleaned_word:
        continue
    if cleaned_word.startswith('а'):
        suitable_words.append(cleaned_word)
if not suitable_words:
    print('Нет совпадений')
    print('Количество: 0')
else:
    for w in suitable_words:
        print(w)
    print(f'Количество: {len(suitable_words)}')
