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

available_words = ['hello','goodbye','zebra','giraffe','mastodon','bizzare','python']
remaining_guess = 8
myword = Word('hello')
print(myword.dictionary)
print(myword)
