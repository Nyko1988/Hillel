# Задача: Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
print('Ex #1')
first = 10
second = 30

print('The result of "+" two digits is ', first + second)
print('The result of "-" two digits is ', first - second)
print('The result of "*" two digits is ', first * second)
print('The result of "/" two digits is ', first / second)
print('The result of "**" two digits is ', first ** second)
print('The result of "%" two digits is ', second % first)
print('The result of "//" two digits is ', second // first)

#Задача: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=)
# чисел з завдання 1. Виведіть на екран результат кожного порівняння.
print('Ex #2')
comparison_result = first < second
print('first < second', 'is', comparison_result)

comparison_result = first > second
print('first > second', 'is', comparison_result)

comparison_result = first == second
print('first == second', 'is', comparison_result)

comparison_result = first!= second
print('first != second', 'is', comparison_result)

#Задача: Створіть змінну - резкльтат конкатенації строк "Hello " та "world!".'''
print('Ex #3')
first_word = 'Hello'
second_word = 'world!'

result_word = '{} {}'.format(first_word, second_word)
print(result_word)