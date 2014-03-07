from passwords import Generator
import unittest


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
        it = self.generator.multiGen(5)
        assert len(list(it)) == 5

if __name__ == '__main__':
    unittest.main()
