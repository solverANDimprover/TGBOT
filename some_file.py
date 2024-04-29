from random import randint
def get_word():
    with open("words_to_play.txt", "r", encoding="utf-8") as file:
        words = file.read().split(", ")
        return words[randint(0, len(words)) - 1]

def add_word():
    word = input("Введите слово, которое хотите добавить в список слов игры")
    with open("words_to_play.txt", "a", encoding="utf-8") as file:
        file.write(f", {word}")
    print("Слово было успешно добавлено")

def guess_word():
    word = get_word()
    

def game():
    try:
        print("Привет, эта игра виселица")
        choice = int(input("1 - начать игру\n2 - пополнить словарь\n"))
        if choice == 1:
            guess_word()
        else:
            add_word()
    except ValueError:
        print("ну ты мудак конечно")

