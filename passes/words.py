from random import choice


class WordCollection:
    def __init__(self, path=None, words=None):
        self.words = []

        if words is not None:
            self.words = self.words + words

        if path is not None:
            with open(path) as f:
                for line in f:
                    self.words.append(line.strip())

    def single_word(self):
        return choice(self.words)

    def iterwords(self, number):
        for i in range(number):
            yield self.single_word()
