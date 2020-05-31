import os
from random import choice
from collections import namedtuple

wordslist_path = "wordslist.txt"

health = namedtuple('health', ['got', 'fail'])
health.got = u'\u2665' # ♥
health.fail = u'\u2661' # ♡

user_tries = 4
user_fails = 0

def health_status_str():
    """Представление количества оставшихся попыток в виде строки вида "♡♥♥♥".
    """
    return ''.join(['♡' if idx < user_fails else health.got for idx in range(user_tries)])

def word_pick(filepath):
    """Выбор случайного слова из файла.
    """
    try:
        with open(filepath) as file:
            lines = [line.strip() for line in file.readlines()]
        return choice(lines).upper()
    except FileNotFoundError:
        return None
        # raise FileNotFoundError("cannot find words list in file \"wordslist.txt\"")
    except IndexError:
        return None
        # raise Exception("wordslist.txt is empty")

def word_guessed_dict_init(word):
    """Словарик, где хранятся буквы загаданного слова и факт их отгадывания.
    """
    return dict(zip(word.upper(), [False]*len(word)))

def word_show_game(word, word_guessed_dict):
    """Строковое представление загаданного слова с учетом отгаданных букв.
    """
    if not word_guessed_dict:
        raise ValueError("word_guessed_dict is empty or not initialized.")
    return ' '.join([ch if word_guessed_dict[ch] else '_' for ch in word])

def guess(char, word_guessed_dict):
    """Функция отгадывания буквы слова. Вернёт True в случае успешной попытки.
    """
    char = char.upper()
    if char in word_guessed_dict and not word_guessed_dict[char]:
        word_guessed_dict[char] = True
        return True
    global user_fails
    user_fails += 1
    return False

def run_game():
    """Геймплей. Выбирается слово, инициализируется словарик отгадываний.
    Выход по заполнению словарика, либо по преодолению порога ошибок.
    """
    word = word_pick(wordslist_path)
    if word is None:
        raise Exception("problem with word picking")

    wgd = word_guessed_dict_init(word)
    while not all(wgd.values()) and user_fails < user_tries:
        print(health_status_str(), word_show_game(word, wgd), end='   ')
        char = input("Try your luck: ")[0] # нужен единственный символ. Толстый палец - не моя проблема.
        guess(char, wgd)
    print(' '.join(word))
    if user_fails < user_tries:
        print('Congratulations!')
    else:
        print('You lose!')


if __name__ == "__main__":
    run_game()
    