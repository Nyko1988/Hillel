#Напишіть функцію, яка приймає два аргументи.
#Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
#Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
#В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
print('Ex. #1')
def compare_elements(first_arg, second_arg):
    if type(first_arg) == type(second_arg):
        if type(first_arg) is str:
            return first_arg + second_arg
        elif type(first_arg) is int:
            return first_arg * second_arg
        else:
            return first_arg, second_arg
    else:
        return first_arg, second_arg

print(compare_elements(3, 2))
print(compare_elements('1', 'd'))
print(compare_elements(2, [1, 3]))
print(compare_elements([1, 3], ['d', 5]))