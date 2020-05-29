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
    return ''.join(['♡' if idx < user_fails else health.got for idx in range(user_tries)])

def word_pick(filepath):
    try:
        with open(filepath) as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return None
    except IndexError:
        return None
    return choice(lines)

def word_guessed_dict_init(word):    
    return dict(zip(word, [False]*len(word)))

def word_show_game(word, word_guessed_dict):
    if not word_guessed_dict:
        raise ValueError("word_guessed_dict is not initialized.")
    return ' '.join([ch if word_guessed_dict[ch] else '_' for ch in word])

def guess(char, word_guessed_dict):
    if char in word_guessed_dict and not word_guessed_dict[char]:
        word_guessed_dict[char] = True
        return True
    global user_fails
    user_fails += 1
    return False

def run_game():
    word = word_pick(wordslist_path)
    wgd = word_guessed_dict_init(word)
    while not all(wgd.values()) and user_fails < user_tries:
        print(health_status_str(), word_show_game(word, wgd), end='   ')
        char = input("Try your luck: ")
        guess(char, wgd)
    print(' '.join(word))
    if user_fails < user_tries:
        print('Congratulations!')
    else:
        print('You lose!')


if __name__ == "__main__":
    run_game()
    