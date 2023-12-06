class Hangman:
    lifes = 7
    def __init__(self,word):
        self.word = word
        self.guessed = ["_"] * len(self.word)
        
    #Return True or False if the letter guessed is correct.
    def guess_word(self,guess):
        if guess not in self.word:
            return False
        return True
    #Reveal letter based on guess
    
    
    
    def reveal_letter(self,letter):
        for i in range(len(self.word)):
            
            if self.word[i] == letter:
                
                self.guessed[i] = letter
        return self.guessed
    
    def wrong_guess(self):
        hang_array = [['|','-','-','|'],
                      ['|',' ',' ','|']]
        return hang_array

    def hide_word(self):
        return self.guessed
        
    
    