from hang import Hangman
word = "abcdeb"
hangman = Hangman(word)
print(hangman.hide_word())
letter_guess = input("Enter: ")
if hangman.guess_word(letter_guess):
    print(hangman.reveal_letter(letter_guess))
else:
    print(hangman.wrong_guess())
#print(hangman.reveal_letter('b'))

