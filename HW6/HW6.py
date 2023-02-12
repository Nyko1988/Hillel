#Напишіть функцію, яка приймає два аргументи.
#Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
#Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
#В будь-якому іншому випадку - функція повертає кортеж з двох агрументів
print('Ex #1:')

def compare_types_of_arguments(fist_arg, second_arg):
    if type(fist_arg) == type(second_arg):
        print(f"You entered the same types: {type(fist_arg)}")
        return True
    print("You entered different types")

def check_types_int_or_str(element):
    if type(element) == int or type(element) == str:
        return True

def multiplication_two_arguments(first_arg, second_arg):
    return first_arg * second_arg

def addition_two_arguments(first_arg, second_arg):
    return first_arg + second_arg

def create_tuple(first_element, second_element):
    return tuple((first_element, second_element))

def main_logic(first_element, second_element):
    if compare_types_of_arguments(first_element, second_element):
        if check_types_int_or_str(first_element):
            if type(first_element) == str:
                result = addition_two_arguments(first_element, second_element)
            else:
                result = multiplication_two_arguments(first_element, second_element)
        else:
            result = create_tuple(first_element, second_element)
    else:
        result = create_tuple(first_element, second_element)
    return result


first_element = [4, 5, 10]
second_element = ['dsd']

result = main_logic(first_element, second_element)
print(f'The result is: {result}')


#Візьміть попереднє дз "Касир в кінотеатрі" і перепишіть за допомогою функцій. Памʼятайте про SRP!
print('Ex #2:')

def age_input():
    age = input('Введіть ваший вік:')
    return age

def age_is_digit(age):
    if age.isdigit():
        return True

def age_in_correct_renge(age):
    if 1 <= age < 100:
        return True

def age_is_seven(age):
    if age.find("7") != -1:
        return True

def age_is_correct(age):
    if age < 7:
        print("Де твої батьки?")
    elif 7 <= age < 16:
        print("Це фільм для дорослих!")
    elif 16 <= age <= 65:
        print("А білетів вже немає!")
    elif 65 < age < 100:
        print("Покажіть пенсійне посвідчення!")

def print_message_not_correct_age():
    print("Введіть будьласка коректний вік")

def cashier_in_cinema():
    while True:
        age = age_input()
        if age.isdigit():
            age_int = int(age)
            if age_in_correct_renge(age_int):
                if age_is_seven(age):
                    print("Вам сьогодні пощастить!")
                else:
                    age_is_correct(age_int)
                break
            else:
                print_message_not_correct_age()
        else:
            print_message_not_correct_age()


cashier_in_cinema()