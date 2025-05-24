# Exercise 2.2: Dictionaries - Word Frequencies
__note__ = ('This is Just an example of how to use dictionaries'
            'A real case will need more imports such as string,'
            'eliminating punctuation and checks')

def word_frequency(text: str) -> dict[str, int]:
    words = text.split()
    result = {}
    for word in words:
        result[str(word)] = words.count(word)
    return result


result = word_frequency('hello my name is hello and, and i am 999 am good years is old')
print(result)