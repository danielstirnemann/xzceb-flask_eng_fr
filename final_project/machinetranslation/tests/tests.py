from translator import englishToFrench, frenchToEnglish
import unittest


class TestTranslator (unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(englishToFrench("hello"),"bonjour")

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish("bonjour"),"hello")


if __name__ == '__main__':
    unittest.main()