#Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]. Напишіть код, який видалить
#(не створить новий, а саме видалить!) з нього всі числа, які менше 21 і більше 74.
print('Ex. #1')
list = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
print('incoming list:', list)
list_copy = list.copy()
for elem in list_copy:
    if 21 > elem or elem > 74 :
        list.remove(elem)
print('updated list:', list)
#Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:
#{ "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "roze-tka": 38.003}.
#Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких потрапляють в діапазон між мінімальною і максимальною ціною.
#Наприклад:
#lower_limit = 35.9
#upper_limit = 37.339
#> match: "x-store", "main-service"
print('Ex. #2')
dict = {
    "cito": 47.999,
    "BB_studio": 42.999,
    "momo": 49.999,
    "main-service": 37.245,
    "buy.now": 38.324,
    "x-store": 37.166,
    "the_partner": 38.988,
    "store": 37.720,
    "roze-tka": 38.003
                        }
lower_limit = 38.0
upper_limit = 60.0
shops_filtered_out = ''
for elem in dict:
    if lower_limit < dict[elem] < upper_limit:
        shops_filtered_out += "'{}', ".format(elem)
print('incoming dictionary:', dict)
print("match:", shops_filtered_out)