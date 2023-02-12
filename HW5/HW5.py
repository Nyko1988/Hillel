"""
Завдання 1
Макс 40 балів
написати програму, яка просить в користувача ввести через пробіл міста, в яких він був за минулі 10 років
потім окремо запросити у користувача міста, куди він хоче поїхати внаступні 10 років
вивести на екран повідомлення з текстом про те, що користувачу, мабуть, дуже сподобалося в містах, які він повторив в
двох циклах вводу, а саме... (сформувати строку, використовуючи join)
якщо повтору не було - вивести повідомлення, що користувач відкритий до чогось нового

врахувати випадки, що користувач нічого не вводить не потрібно, в даному випадку вам явно зазначено,
що ці перевірки не потрібні.
не потрібно перевіряти введення цифр
ми виходим із того, що користувач введе щось на зразок "Київ Тернопіль париЖ акапулько-80"

В той же час врахуйте, що користувач може вводити дані в різних регістрах

використати сети!!!"""
cities_was = set((input('Enter cities you\'ve been to in the past 10 years, using a space: ')).lower().split())
cities_want = set(input("Enter cities where you want to go in the next 10 years: ").lower().split())
common_cities = cities_was.intersection(cities_want)
if common_cities:
    print('You probably liked it a lot in the following cities: ', ', '.join(common_cities),'.')
else:
    print("You are open to something new")


print()
"""
Завдання 2
макс 60 балів
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку 
здійснюється за механізмом 
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення, 
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}
# ваш код нижче
from pprint import pprint

new_student_name = 'Микитюк'
student[new_student_name] = {
                'Пошта': 'test@gmail.com',
                'Номер телефону': +3809959595959,
                'Вік': 35,
                'Середній бал': 90.5
                            }
print(f'New student "{new_student_name}" with follow datas was created:', student['Микитюк'])

full_score = 0
for person in student:
    full_score += student[person]['Середній бал']
    if student[person]['Середній бал'] > 90:
        print(f"Student '{person}' has an average score '{student[person]['Середній бал']}' ")
    if student[person]['Номер телефону'] == None:
        student[person]['Номер телефона батьків'] = '+380900000000'
        print( f'Student "{person}", your phone will be phone of your parents "{student[person]["Номер телефона батьків"]}"')

print('Average score of whole group is:', full_score/len(student))
pprint(student)

