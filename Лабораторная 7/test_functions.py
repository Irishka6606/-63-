from functions import average, normalize_text, sum_digits, select_numbers

assert sum_digits(0) == 0
assert sum_digits(507) == 12
assert sum_digits(-507) == 12
assert average([]) is None
assert average([2, 4, 6]) == 4
assert normalize_text('  ПРИВЕТ   МИР  ') == 'привет мир'
assert normalize_text('   ') == ''

actual = average([1, 2])
assert abs(actual - 1.5) < 1e-9

control_list = [-5, 0, 2, 5]
assert select_numbers(control_list, 2) == [5]
assert select_numbers([], 2) == []
assert select_numbers([1, 2, 3], 2) == [3]
assert select_numbers([5, 2, 5, 1], 2) == [5, 5]

copy_before = control_list.copy()
select_numbers(control_list, 2)
assert control_list == copy_before

def is_palindrome(text):
    normalized = normalize_text(text)
    if not normalized:
        return False
    return normalized == normalized[::-1]

assert is_palindrome('12321') is True
assert is_palindrome('Привет мир') is False
assert is_palindrome('') is False
assert is_palindrome('    ') is False
print('Все проверки пройдены успешно!')