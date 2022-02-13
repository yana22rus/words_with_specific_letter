from random import choice

vowels = ["а", "е", "и", "о", "у", "э", "ю", "я"]

consonants = ["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

all_letters = vowels + consonants


def options(choice_letter):

    letter = choice(choice_letter).lower()

    print(f"Вы загодали букву {letter}")

    return {"flag":False,"letter": letter}

flag = True

while flag:

    str_input = input("Какую букву загадать\n 1 - случайная гласная\n 2 - случайна согласная\n 3 - случайная гласная+согласная\n 4 - задать букву самому\n")
    if str_input == "1":
        data = options(vowels)
        letter = data["letter"]
        flag = data["flag"]


    if str_input == "2":
        data = options(consonants)
        letter = data["letter"]
        flag = data["flag"]


    if str_input == "3":
        data = options(all_letters)
        letter = data["letter"]
        flag = data["flag"]


    if str_input == "4":
        letter = input()

        if letter == "" or letter == " ":
            print("Пустой символ это не буква")
            continue
        else:
            letter = list(letter)[0].lower()
            print(f"Вы загодали букву {letter}")
            break

input_letters = input()

lst_letters = []

while input_letters != ":q":

    if input_letters[0].lower() != letter:

        print("Указывайте только те буквы которые были выбраны для игры")

    else:

        if input_letters not in lst_letters:

            lst_letters.append(input_letters)

            print(f"Вы указали на данную буквы {len(lst_letters)} слов")

        else:
            print("Данное слово вы уже указывали")

    input_letters = input()
