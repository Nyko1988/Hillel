#Напишіть функцію, яка приймає два аргументи.
#Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
#Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
#В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
print('Ex. #1')
def compare_elements(first_arg, second_arg):
    if type(first_arg) == type(second_arg):
        if type(first_arg) == str:
            return first_arg + second_arg
        elif type(first_arg) == int:
            return first_arg * second_arg
        else:
            return first_arg, second_arg
    else:
        return first_arg, second_arg

print(compare_elements(3, 2))
print(compare_elements('1', 'd'))
print(compare_elements(2, [1, 3]))
print(compare_elements([1, 3], ['d', 5]))


#Візьміть попереднє дз "Касир в кінотеатрі" і перепишіть за допомогою функцій. Памʼятайте про SRP!
"""Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік (можно використати константу або функцію input(), 
на екран має бути виведено лише одне повідомлення, також подумайте над варіантами, коли введені невірні дані).
якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!" """
print('Ex. #2')

def age_input():
    while True:
        age = input('Введіть ваш вік: ')
        try:
            age_int = int(age)
        except ValueError:
            print('Будь ласка введіть корректний вік')
            continue
        if 1 > age_int or 100 < age_int:
            print('Будь ласка введіть корректний вік')
            continue
        else:
            return age_int

def compare_age(age):
    message = ''
    if str(age).find("7") != -1:
        message = "Вам сьогодні пощастить!"
    elif age < 7:
        message = "Де твої батьки?"
    elif 7 <= age < 16:
        message = "Це фільм для дорослих!"
    elif 16 <= age <= 65:
        message = "А білетів вже немає!"
    elif 65 < age < 100:
        message = "Покажіть пенсійне посвідчення!"
    return message

def cashier_in_cinema():
    age = age_input()
    print(compare_age(age))


cashier_in_cinema()


