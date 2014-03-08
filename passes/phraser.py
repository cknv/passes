from .mutators import mutate


class Phraser:
    def __init__(self, mutate_rate=0.5):
        self.mutate_rate = mutate_rate

    def generate(self, number):
        return ' '.join(self.iterword(number))

    def iterword(self, number):
        for i in range(number):
            word = ''.join(mutate('hello', rate=self.mutate_rate))
            yield word
