def season_by_date(date):
    """
    This function determines the season by date. The function receives a string in the
    format "[day].[month]" (eg "12.01", "30.08", "1.11", etc.) and returns a string with the corresponding
    season to which this date belongs ("summer", "autumn" , "winter", "spring"). If the function receives an incorrect
    day or month as an input, it returns the corresponding message.

    Args:
        date (str):

    Returns:
        (str)
    """
    day = int(date[:(date.index('.'))])
    month = int(date[(date.index('.')+1):])

    if 1 > day or day > 31:
        result = 'incorrect day'
        return result

    seasons = {
        'Зима': [12, 1, 2],
        'Весна': [3, 4, 5],
        'Літо': [6, 7, 8],
        'Осінь': [9, 10, 11],
                             }
    result = 'incorrect month'
    for season in seasons:
        if month in seasons[season]:
            result = season
    return result

def calculator(first_digit, second_digit, operation):
    """
        The function accepts two numeric arguments and a string, which is responsible for the operation between them (+ - / *).
        The function returns the value of the corresponding operation (addition, subtraction, division, multiplication),
        other operations are not allowed.
        If the function received an invalid data type for the operation (not a number) or
        an invalid (unknown) type of operation, it returns None and displays the message "Invalid data type".
    Args:
        first_digit (float):
        second_digit(float):
        operation(str):

    Returns:
        (float)
    """
    first_digit = float(first_digit)
    second_digit = float(second_digit)
    support_opperations = ('+', '-', '/', '*')

    if type(operation) != str:
        print("Невірний тип даних")
        return None

    if operation in support_opperations:
        if operation == '*':
            result_of_operations = first_digit * second_digit
        elif operation == '-':
            result_of_operations = first_digit - second_digit
        elif operation == '+':
            result_of_operations = first_digit + second_digit
        elif operation == '/':
            if second_digit == 0:
                print("Операція не підтримується")
                return None
            else:
                result_of_operations = first_digit / second_digit
        return result_of_operations
    else:
        print("Операція не підтримується")

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
    result_message = compare_age(age)
    return result_message