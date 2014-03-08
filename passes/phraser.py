from .mutators import mutate
from .words import WordCollection


class Phraser:
    def __init__(self, word_file_path, mutate_rate=0.5):
        self.mutate_rate = mutate_rate
        self.words = WordCollection(path=word_file_path)

    def generate(self, number):
        phrase = ' '.join(self.iterword(number))
        return mutate(phrase)

    def iterword(self, number):
        for word in self.words.iterwords(number):
            yield word
