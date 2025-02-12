import unittest
from Sort import data_generator
from Sort import constants


class DataGeneratorTest(unittest.TestCase):
    def test_data_generator_with_empty_list(self):
        n = 0
        random_list = data_generator.get_random_list(n)
        self.assertEqual(n, len(random_list))

    def test_data_generator_with_1(self):
        n = 1
        random_list = data_generator.get_random_list(n)
        self.assertEqual(n, len(random_list))

    def test_data_generator_with_2(self):
        n = 2
        random_list = data_generator.get_random_list(n)
        self.assertEqual(n, len(random_list))

    def test_data_generator_with_1000(self):
        n = 1000
        random_list = data_generator.get_random_list(n)
        self.assertEqual(n, len(random_list))
        for number in random_list:
            self.assertLessEqual(number, constants.MAX_VALUE)
            self.assertGreaterEqual(number, 0)


if __name__ == "__main__":
    unittest.main()
