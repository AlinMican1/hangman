from hang import Hangman
word = "abcdeb"
hangman = Hangman(word)
hangman.lifes -= 1

print(hangman.hide_word())
while hangman.lifes >= 0:
    letter_guess = input("Enter: ")
    if hangman.guess_word(letter_guess):
        print(hangman.reveal_letter(letter_guess))
    else:
        
        print(hangman.wrong_guess(hangman.lifes))
        hangman.lifes -= 1