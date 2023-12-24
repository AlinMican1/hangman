class Hangman:
    lifes = 6
    correct_letter = 0

    def __init__(self, word):
        self.word = word
        self.guessed = ["_"] * (len(self.word) - 1)
        self.array = ["_", "_", "_", "_", "_", "_", "_"]
        self.hang_array = [
            [" ", "|", "-", "|"],
            [" ", "|", " ", "|"],
            [" ", " ", " ", "|"],
            [" ", " ", " ", "|"],
            [" ", " ", " ", "|"],
            [" ", " ", " ", "|"],
            [" ", " ", " ", "|"],
            ["_", "_", "_", "|"],
        ]
        self.right_words = set()

    # Return True or False if the letter guessed is correct.
    def guess_word(self, guess):
        if guess not in self.word:
            return False
        return True

    # Reveal letter based on guess
    def reveal_letter(self, letter):
        for i in range(len(self.word)):
            if self.word[i] == letter and letter not in self.right_words:
                self.guessed[i] = letter
                self.right_words.add(letter)
                self.correct_letter += 1
            

        return " ".join(self.guessed)

    def guessed_letters(self, letter):
        return letter

    def wrong_guess(self, lifes):
        body_part_location = [
            [5, 2],
            [5, 0],
            [4, 1],
            [3, 2],
            [3, 0],
            [3, 1],
            [2, 1],
        ]
        body_part = [
            "\\",
            "/",
            "|",
            "\\",
            "/",
            "|",
            "O",
        ]
       

        # for row in hang_array:
        #     print(" ".join(row))

        rows, cols = body_part_location[lifes]

        self.hang_array[rows][cols] = body_part[lifes]

        hang_visual = ""
        for row in self.hang_array:
            hang_visual += f"{" ".join(row)}\n"

        return hang_visual
        # string = "WRONG!!"
        # string = string[::-1]
        # self.array[lifes] = string[lifes]

        # return " ".join(self.array[::-1])

    def hide_word(self):
        return self.guessed
