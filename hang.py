class Hangman:
    lifes = 7
    correct_letter = 0

    def __init__(self, word):
        self.word = word
        self.guessed = ["_"] * (len(self.word) - 1)

    # Return True or False if the letter guessed is correct.
    def guess_word(self, guess):
        if guess not in self.word:
            return False
        return True

    # Reveal letter based on guess
    def reveal_letter(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                correct_letter += 1
                self.guessed[i] = letter
        return " ".join(self.guessed)

    def wrong_guess(self, lifes):
        array = ["_", "_", "_", "_", "_", "_", "_"]
        string = "WRONG!!"
        string = string[::-1]
        array[lifes] += string[lifes]

        return " ".join(array[::-1])

    def hide_word(self):
        return self.guessed
