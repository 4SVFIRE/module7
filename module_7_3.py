import string
from string import punctuation


class WordsFinder:
    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        punctuation_text = str.maketrans('', '', string.punctuation)
        for file_name in self.file_names:
            with open(file_name,'r', encoding= 'utf-8') as file:
                all_words[file_name] = []
                for line in file:
                    line = line.lower()
                    line = line.translate(punctuation_text)
                    all_words[file_name].extend(line.split())
        return all_words

    def find(self, word):
            word = word.lower()
            result = {}
            for file_name, words in self.get_all_words().items():
                if word in words:
                    result[file_name] = words.index(word) + 1
            return result

    def count(self, word):
        word = word.lower()
        result = {}
        for file_name, words in self.get_all_words().items():
            count = words.count(word)
            if count > 0:
                result[file_name] = count
        return result



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
