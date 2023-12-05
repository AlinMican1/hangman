from hang import Hangman
word = "abcdef"
hangman = Hangman(word)
if hangman.guess_word('l'):
    print(hangman.correct_guess('b'))