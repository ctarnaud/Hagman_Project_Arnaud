import random
import time
import re
from utils.game import Hangman

def main():
    self.count
    self.well_guessed_letter
    self.word_to_find
    self.well_guessed_letters
    self.already_guessed
    self.length
    self.play_game
    possible_word = ['becode', 'learning', 'mathematics', 'sessions']

    word_to_find = list(random.choice(possible_word))
    lenth = len(word_to_find)
    well_guessed_letter = "_" * lenth
    turn_count = 0
    already_guessed_letters = []
    play_game = ""

def play():
    self.play_game
    play_game = input("Want to play? y = yes, n = no \n")
    while play_game not in ["y", "n", "Y", "N"]
        play_game = input("Want to play? y = yes, n = no \n")
    if play_game == "y":
        main()
    elif play_game == "n"
        print("Sorry, see you soon")
        exit()
def hangman():
    self.count
    self.well_guessed_letter
    self.word_to_find
    self.well_guessed_letters
    self.already_guessed
    self.length
    self.play_game
    word_to_find = list(random.choice(possible_word))
    lenth = len(word_to_find)
    well_guessed_letter = "_" * lenth
    turn_count = 0
    already_guessed_letters = []
    play_game = ""
    limit = 5
    guess = input("Enter letter: \n")
    guess = guess.strip()
    if len(guess.strip(1)) == 0 or len(guess.strip(1)) >= 2 or guess <= "9"
        print("Wrong: \n")
        hangman()
    elif guess in word_to_find:
        already_guessed_letters.extend([guess])
        index = word_to_find.find(guess)
        word_to_find = word_to_find[:index] + "_" + word_to_find[index + 1:]
        print(well_guessed_letter + "\n")
    elif guess in already_guessed_letters:
        print("Try again.\n")
    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print("-----\n"
                  "l    \n"
                  "l    \n"
                  "_l_  \n")
            print("Wrong." + str(limit-count) + "guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print(("-----\n"
                  "l    \n"
                  "l    \n"
                  "_l_  \n")
        elif count == 3:
            time.sleep(1)
            print("-----\n"
                  "l    \n"
                  "l    \n"
                  "_l_  \n")
            print("Wrong." + str(limit-count) + "guesses remaining\n")
        elif count == 4: 
            time.sleep(1)
            print("-----\n"
                  "l    \n"
                  "l    \n"
                  "_l_  \n")
            print("Wrong." + str(limit-count) + "guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print("-----\n"
                  "l    \n"
                  "l    \n"
                  "_l_  \n")
            print("Wrong. You are hanged")
            play()
        if word_to_find == "_" * length:
            print("Great")
            play()
        elif count != length:
            hangman()
main()
hangman()
