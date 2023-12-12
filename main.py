import random

from hang import Hangman

# Open the file and read the words from it

with open("hangman_words.txt", "r") as file:
    words = file.readlines()

file.close()

# Store all words in an array
word_list = []
for word in words:
    word_list.append(word)
random_word = random.randint(0, (len(words) - 1))


print(word_list[random_word])
# Put the random word into hangman guessing
word = word_list[random_word]
hangman = Hangman(word)
hangman.lifes -= 1
#Print the blank of how many words the user needs to guess.
print(f"{" ".join(hangman.hide_word())}\n")

while hangman.lifes >= 0:
    letter_guess = input("Enter a letter to guess: ")
    if hangman.guess_word(letter_guess):
        
        print(hangman.reveal_letter(letter_guess))
        hangman.correct_guess += 1
        print(hangman.correct_guess)
    else:
        print(hangman.wrong_guess(hangman.lifes))
        hangman.lifes -= 1

