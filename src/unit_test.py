import unittest
from main import number_to_french_words


class TestFrenchWord(unittest.TestCase):

    def test_single_digit_conversion(self):
        self.assertEqual(number_to_french_words(13), "treize")

    def test_tens_and_units_conversion(self):
        self.assertEqual(number_to_french_words(68), "soixante-huit")

    def test_hundreds_conversion(self):
        self.assertEqual(number_to_french_words(789), "sept-cent-quatre-vingt-neuf")

    def test_large_number_conversion(self):
        self.assertEqual(number_to_french_words(99999), "quatre-vingt-dix-neuf-mille-neuf-cent-quatre-vingt-dix-neuf")

    def test_hundred_conversion(self):
        self.assertEqual(number_to_french_words(100), "cent")

    def test_thousands_conversion(self):
        self.assertEqual(number_to_french_words(5005), "cinq-mille-cinq")
        

    def test_negative_number_error(self):
        with self.assertRaises(ValueError):
            number_to_french_words(-10)

    def test_decimal_number_error(self):
        with self.assertRaises(ValueError):
            number_to_french_words(3.14)



if __name__ == '__main__':
    unittest.main()
