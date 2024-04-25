def is_balanced(expression):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    matching_brackets = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            # Перевірка, чи стек порожній та останній відкриваючий розділювач відповідає поточному закриваючому
            if not stack or stack[-1] != matching_brackets[char]:
                return False
            stack.pop()  # Видаляємо відповідний відкриваючий розділювач зі стеку

    # Перевірка, чи стек порожній після проходження всього виразу
    return not stack

# Приклади використання:
print(is_balanced("(12){2-3}[]"))  # True
print(is_balanced("({1[3-5}])"))   # False
print(is_balanced("()(1){23}{[2()()]}"))  # True