from random import random, choice

lookup = {
    'a': '4@',
    'i': '!1',
    'o': '0',
    ' ': '_-',
    '': '',
}


def mutate(word, rate=0.5):
    for char in word:
        if char in lookup and random() > rate:
            yield choice(lookup[char])
        else:
            yield char
