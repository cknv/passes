from passes import Generator, multi_gen, Phraser
import unittest
import re


class TestGeneratorNoCharset(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()

    def test_generate(self):
        self.chars = set(self.generator.chars)
        for i in range(1000):
            res = self.generator.generate(10)
            self.chars = self.chars - set(res)
        assert len(self.chars) == 0


class TestResultLength(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()

    def test_result_length(self):
        res = self.generator.generate(10)
        assert len(res) == 10


class TestIteration(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()

    def test_iteration(self):
        it = multi_gen(5)
        assert len(list(it)) == 5


class TestPhraseGeneration(unittest.TestCase):
    def setUp(self):
        word_file = '/usr/share/dict/words'
        self.phraser = Phraser(word_file)

    def test_phrase(self):
        phrase = self.phraser.generate(5)
        words = re.split(r'[ _-]', phrase)
        assert len(words) == 5

if __name__ == '__main__':
    unittest.main()
