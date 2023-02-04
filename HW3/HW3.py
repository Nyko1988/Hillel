#Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о" (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".
print("Ex. #1")
while True:
    word = input("Please enter word which contains leetter 'o': ")
    if word.casefold().find('o') != -1:
        print(f"you entered word '{word}' which contains leetter 'o'")
        break

    print("Try again")

#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який сформує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Зауважте, що lst1 не є статичним і може формуватися динамічно від запуску до запуску.
print("Ex. #2")
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for elem in lst1:
    if type(elem) == str:
        lst2.append(elem)

print(lst2)

#Є стрінг з певним текстом (можна скористатися input або константою).
# Напишіть код, який визначить кількість слів в цьому тексті, які закінчуються на "о" (враховуються як великі так і маленькі).
print("Ex. #3")
import re
sentence = "I've always thoughto that the only sentence that uses all the letters of the \n" \
           "alphabet was \"The quick brown fox jumps over the lazy dogo.\" Is there another ono?"
sentence_cleared = re.sub( r'\W', ' ', sentence)
print(sentence_cleared)
number_of_words = 0
word_list = sentence_cleared.split()
for i in word_list:
    if i[-1].casefold() == 'o':
        number_of_words += 1

print(number_of_words)