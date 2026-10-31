def sum_digits(number):
    number = abs(number)
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def normalize_text(text):
    return ' '.join(text.split()).lower()

def select_numbers(numbers, threshold):
    result = []
    for num in numbers:
        if num > threshold:
            result.append(num)
    return result

def is_palindrome(text):
    normalized = normalize_text(text)
    if not normalized:
        return False
    return normalized == normalized[::-1]