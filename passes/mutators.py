from random import random, choice

lookup = {
    'a': '4@',
    'i': '!1',
    'o': '0',
    ' ': '_-',
    '': '',
}


def mutate(word, rate=0.5):
    mutated_chars = []
    for char in word:
        if char in lookup and random() > rate:
            mutated_chars.append(choice(lookup[char]))
        else:
            mutated_chars.append(char)
    return ''.join(mutated_chars)
