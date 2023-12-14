class Hangman:
    lifes = 6
    correct_letter = 0

    def __init__(self, word):
        self.word = word
        self.guessed = ["_"] * (len(self.word) - 1)
        self.array = ["_", "_", "_", "_", "_", "_", "_"]

    # Return True or False if the letter guessed is correct.
    def guess_word(self, guess):
        if guess not in self.word:
            return False
        return True

    # Reveal letter based on guess
    def reveal_letter(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter:
                self.guessed[i] = letter
                self.correct_letter += 1

        return " ".join(self.guessed)

    def guessed_letters(self, letter):
        return letter

    def wrong_guess(self, lifes):
        string = "WRONG!!"
        string = string[::-1]
        self.array[lifes] = string[lifes]

        return " ".join(self.array[::-1])

    def hide_word(self):
        return self.guessed
