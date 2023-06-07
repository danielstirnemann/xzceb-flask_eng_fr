"""This Module translates Text"""

from deep_translator import MyMemoryTranslator


def englishToFrench(english_text):
    """This Method translates from english to french"""
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text


def frenchToEnglish(french_text):
    """This Method translates from french to english"""
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text


print(englishToFrench("hello"))
print(frenchToEnglish("bonjour"))
