#Сформуйте стрінг, в якому міститься інформація про певне слово.
# "Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters",
# наприклад "Word 'Python' has 6 letters". Для отримання слова для аналізу скористайтеся константою або функцією input().
print("Ex. №1")
word = input('Please enter word:')
word_length = len(word)
sentence = 'Word "{}" has {} letters'.format(word, word_length)
print(sentence)

"""Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік (можно використати константу або функцію input(), 
на екран має бути виведено лише одне повідомлення, також подумайте над варіантами, коли введені невірні дані).
якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!" """
print("Ex. №2")
while True:
    age_input = input('Введіть ваший вік:')
    if age_input.isdigit():
        age_input_digit = int(age_input)
        if 1 <= age_input_digit < 100:
            if age_input.find("7") != -1:
                print("Вам сьогодні пощастить!")
                break
            else:
                if age_input_digit < 7:
                    print("Де твої батьки?")
                    break
                elif 7 <= age_input_digit < 16:
                    print("Це фільм для дорослих!")
                    break
                elif 16 <= age_input_digit <= 65:
                    print("А білетів вже немає!")
                    break
                elif 65 < age_input_digit < 100:
                    print("Покажіть пенсійне посвідчення!")
                    break
        else:
            print("Введіть будьласка коректний вік")
    else:
        print("Введіть будьласка коректний вік")

