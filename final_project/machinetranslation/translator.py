from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):
    frenchText = MyMemoryTranslator(source='english', target='french').translate(englishText)
    return frenchText


print(englishToFrench("hello"))