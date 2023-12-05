class Hangman:
    
    def __init__(self,word):
        self.word = word

    #Return True or False if the letter guessed is correct.
    def guess_word(self,guess):
        if guess not in self.word:
            return False
        return True
    
    def correct_guess(self,guess):
        if guess:
            return guess
        return 0
