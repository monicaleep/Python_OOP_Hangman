class Word():
    def __init__(self, chosen_word):
        word_dict = []
        for letter in chosen_word:
            word_dict.append({'letter': letter, 'guessed': False})
        self.dictionary = word_dict

    def __str__(self):
        text = ""
        for item in self.dictionary:
            if item['guessed']:
                text += item['letter']
            else:
                text += "_ "
        return text

    def checkLetter(self, letter):
        flag = False
        for item in self.dictionary:
            if item['letter'] == letter:
                item['guessed'] = True
                flag = True
        return flag

    def checkFinished(self):
        for item in self.dictionary:
            if not item['guessed']:
                return False
                break
        return True


available_words = ['hello', 'goodbye', 'zebra', 'giraffe', 'mastodon',
                   'bizzare', 'python']
remaining_guess = 8
gameOver = False
guessed_letters = []
myword = Word('hello')  # TODO use getRandomWord here


def getRandomWord(available_words):
    # TODO get random word from available_words
    pass


def handle_guess(letter):
    letter = letter.lower()
    if len(letter) > 1:
        print('too long!')
        return
    elif not letter.isalpha():
        print("Only letters are valid entries, try again.")
        return
    elif letter in guessed_letters:
        print('You already guessed the letter', letter)
    else:
        guessed_letters.append(letter)
        global remaining_guess
        remaining_guess -= 1
        print('You have this many guesses left:', remaining_guess)
        flag = myword.checkLetter(letter)
        if not flag:
            print('Wrong! The letter', letter, 'is not in the word.')
        global gameOver
        gameOver = myword.checkFinished()


#  game engine
print("Welcome to hangman, you will have", remaining_guess, "guesses to get the word. Type 'quit' to quit at any time.")
while True:
    print(myword)
    if gameOver:
        print('You won!')
        break
    elif remaining_guess == 0:
        print('You ran out of guesses, sorry!')
        break
    print("Guess a letter", end=": ")
    user_input = input()
    if user_input.lower() == "quit":
        print("bye!")
        break
    else:
        handle_guess(user_input)
