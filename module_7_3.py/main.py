class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}    # список из всех слов текста без знаков препинания
        words = []
        punct_n = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for f_n in self.file_names:
            with open(f_n, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.lower()
                    for symbol in punct_n:
                        line = line.replace(symbol, '' if symbol != ' - ' else ' ')
                    words.extend(line.split())
                all_words[f_n] = words
        return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for f_n, words in self.get_all_words().items():
            if word in words:
                result[f_n] = words.index(word) + 1      # - index позиции слова
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for f_n, words in self.get_all_words().items():
            result[f_n] = words.count(word)   # количество совпадений
        return result


txt_ = WordsFinder('test_file.txt')  # имя файла с исследуемым текстом
print(txt_.get_all_words())     # Печатаем все слова [...] из списка all_words
print(txt_.find('TEXT'))        # Печатаем № позиции слова {'...': x} при первом совпадении
print(txt_.count('teXT'))       # Печатаем количество совпадений {'...': x} в тексте

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))