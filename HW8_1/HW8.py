#Напишіть декоратор, який визначає час виконання функції. Заміряйте час Виконання функцій з попереднього ДЗ
from time import time

def time_decor(function):
    '''
        this decorator determines the execution time of the function and then displays it accordingly
    Args:
        function(def):

    Returns:
        def()
    '''
    def decor(*args, **kwargs):
        start_time = time()
        result = function(*args, **kwargs)
        finish_time = time()
        time_result = finish_time - start_time
        print(f'Function execution time is {time_result}')
        return result
    return decor

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

@time_decor
def cashier_in_cinema():
    age = age_input()
    result_message = compare_age(age)
    return result_message

print('Ex. #1')
cashier_in_cinema()
#Візьміть функції з попереднього ДЗ, покладіть їх у файл lib.py і імпортуйте в основний файл для виконання
import lib

print('Ex. #2')
print(lib.calculator(5, 6, '-'))
print(lib.season_by_date('1.11'))

