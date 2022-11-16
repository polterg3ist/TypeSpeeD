# This is a console application for testing your typing speed
import time
import os
from random import shuffle
from sys import exit


def main():
    work = True
    print('This is a console application for testing your typing speed\n')
    while work:
        os.system('cls')
        langs = os.listdir('languages/')
        print(f"Supported languages is: ")
        for ind, lang in enumerate(langs):
            print(f"{ind+1}. {lang[:-4]}")
        lang_id = input('\nPlease select any language by entering its number: ')

        if lang_id.isdigit() and len(langs) + 1 > int(lang_id) > 0:
            lang_id = int(lang_id) - 1
            print(f"Chosen language is {langs[lang_id][:-4]}")
            while True:
                os.system('cls')
                total_entered = []
                total_words = []
                with open(f"languages/{langs[lang_id]}") as file:
                    words = file.readlines()
                shuffle(words)

                print("Press enter when you ready")
                input()
                start_time = time.time()

                for i in range(70):
                    os.system('cls')
                    current_time = time.time()
                    time_diff = current_time - start_time
                    if time_diff > 60:
                        break
                    word = words.pop()
                    print(f"{i+1:<5} {word:>5}")
                    entered = input(">>> ")
                    total_entered.append(entered)
                    total_words.append(word.rstrip())

                end_contest(total_entered, total_words, time_diff)

                print(f"\n1. Exit\n2. Change language\n3. Try again\n")
                ans = input('>>>')
                if ans == '1':
                    exit()
                elif ans == '2':
                    break
        else:
            print("[WRONG USER INPUT]")


def end_contest(entered, all_words, taken_time):
    os.system('cls')        # Clear console
    total_syms = sum(len(word) for word in all_words)
    correct_syms, correct_words, incorrect_words = typo_check(entered, all_words)
    wpm, spm = calc_speed(taken_time, correct_syms, correct_words)     # wpm (Words Per Minute), spm (Symbols Per Minute)

    print("[CONTEST FINISHED]")
    print(f"Taken time: {taken_time:.1f}\nTotal symbols: {total_syms}\nCorrect symbols: {correct_syms}")
    print(f"Correct words: {len(correct_words)}\nIncorrect words: {len(incorrect_words)}")
    print(f"Words per minute: {wpm:.1f}\nSymbols per minute: {spm:.1f}")


def typo_check(entered, right):
    correct_words = []
    incorrect_words = []

    for word, correct in zip(entered, right):
        if word == correct:
            correct_words.append(word)
        else:
            incorrect_words.append(word)

    correct_syms = sum(len(word) for word in correct_words)
    return correct_syms, correct_words, incorrect_words


def calc_speed(taken_time, syms, words):
    wpm = len(words) / taken_time * 60
    spm = syms / taken_time * 60

    return wpm, spm


if __name__ == '__main__':
    main()
