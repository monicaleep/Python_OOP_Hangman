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
        for item in self.dictionary:
            if item['letter'] == letter:
                item['guessed'] = True


available_words = ['hello', 'goodbye', 'zebra', 'giraffe', 'mastodon',
                   'bizzare', 'python']
remaining_guess = 8
gameOver = False
guessed_letters = []


def getRandomWord(available_words):
    pass


myword = Word('hello')
print(myword.dictionary)
print(myword)


def handle_guess(letter):
    letter = letter.lower()
    if len(letter) > 1:
        print('too long!')
        return
    elif letter in guessed_letters:
        print('You already guessed the letter', letter)
    else:
        guessed_letters.append(letter)
        global remaining_guess
        remaining_guess -= 1
        print(remaining_guess)
        myword.checkLetter(letter)


#  game engine
while True:
    print(myword)
    print("Guess a letter", end=": ")
    user_input = input()
    handle_guess(user_input)
    if(user_input == "q"):
        print("bye!")
        break
    else:
        print("you typed:", user_input)
