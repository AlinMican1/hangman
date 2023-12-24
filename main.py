import random

from hang import Hangman

# Open the file and read the words from it

with open("hangman_words.txt", "r") as file:
    words = file.readlines()


# Store all words in an array
word_list = []
for word in words:
    word_list.append(word)
random_word = random.randint(0, (len(words) - 1))


print(word_list[random_word])
# Put the random word into hangman guessing
word = word_list[random_word]
hangman = Hangman(word)

#Print the blank of how many words the user needs to guess.
print(f"{" ".join(hangman.hide_word())}\n")

wrong_ans = set()
while hangman.lifes >= 0 and hangman.correct_letter != (len(word) - 1):
    letter_guess = input("Enter a letter to guess: ")
    
    
    if hangman.guess_word(letter_guess):
        print(hangman.reveal_letter(letter_guess))
        
    else:
        print(hangman.wrong_guess(hangman.lifes))
        wrong_ans.add( hangman.guessed_letters(letter_guess))
        
        hangman.lifes -= 1
    print(f"The wrong letters are: {wrong_ans}")


if hangman.correct_letter == (len(word) - 1):
    print("WELL DONE YOU WON NOTHING :)")
        
if hangman.lifes == -1:
    print(f"GAME OVER!!! \nTHE WORD WAS: {word}")
