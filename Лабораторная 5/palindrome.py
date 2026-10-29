text = input('Введите текст:')
clean_text = text.lower().replace(' ', '')

if not clean_text:
    print('Нет текста')
else:
    if clean_text == clean_text[::-1]:
        print('Палиндром')
    else:
        print('Не палиндром')

is_palindrome_loop = True
for i in range(len(clean_text) // 2):
    if clean_text[i] != clean_text[-1 - i]:
        is_palindrome_loop = False
        break
print(f'Проверка циклом: {'Палиндром' if is_palindrome_loop else 'Не палиндром'}')