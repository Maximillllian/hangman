# Write your code here
import random
import re


def menu():
    while True:
        action = input('Type "play" to play the game, "exit" to quit: ')
        if action == 'play':
            hangman()
        elif action == 'exit':
            break


def hangman():
    print('H A N G M A N')
    words = ['python', 'java', 'kotlin', 'javascript']
    right_word = random.choice(words)
    secret_word = '-' * len(right_word)
    user_letters = set()
    lives = 8
    while lives != 0 and secret_word != right_word:
        print()
        print(secret_word)
        user_letter = input('Input a letter:')
        if user_letter in user_letters:
            print('You already typed this letter')
        elif len(user_letter) != 1:
            print('You should input a single letter')
        elif not user_letter.isascii() or not user_letter.islower():
            print('It is not an ASCII lowercase letter')
        elif user_letter in right_word:
            index = [m.start() for m in re.finditer(user_letter, right_word)]
            for i in index:
                lst = list(secret_word)
                lst[i] = user_letter
                secret_word = ''.join(lst)
            user_letters.add(user_letter)
        else:
            lives -= 1
            print('No such letter in the word')
            user_letters.add(user_letter)
    if lives == 0:
        print('You are hanged!\n')
    else:
        print(f'''\n{secret_word}
You guessed the word!
You survived!\n''')


if __name__ == '__main__':
    menu()
