from translator import english_to_french, french_to_english
import unittest


class TestTranslator (unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(english_to_french("hello"),"bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("bonjour"),"hello")


if __name__ == '__main__':
    unittest.main()