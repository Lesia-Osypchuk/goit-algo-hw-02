from collections import deque

def is_palindrome(input_string):
    # Перетворюємо вхідний рядок на список символів, усуваємо пробіли та перетворюємо на нижній регістр
    input_string = input_string.replace(" ", "").lower()
    
    # Створюємо двосторонню чергу (deque) та додаємо символи з вхідного рядка
    char_queue = deque(input_string)
    
    # Порівнюємо символи з обох кінців черги до тих пір, поки черга не опустіє або досягне середини
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    return True

# Приклади використання:
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
print(is_palindrome("Able was I ere I saw Elba"))
print(is_palindrome("Madam in Eden Im Adam"))
print(is_palindrome("My name is Anna"))