from string import digits, ascii_letters, punctuation
from random import choice


def multi_gen(number, length=10):
    generator = Generator()
    for i in range(number):
        yield generator.generate(length)


class Generator:
    def __init__(self, charset=None):
        if charset is None:
            charset = ascii_letters + digits + punctuation
        self.chars = charset

    def generate(self, length=10):
        return ''.join([choice(self.chars) for i in range(length)])
