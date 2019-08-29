from nltk.tokenize import word_tokenize


class Corpus:

    corpus_data = []

    def __init__(self, corpus_file):

        with open(corpus_file, 'r') as my_file:
            data_en = my_file.read().replace('\n', ' ')\
                .replace(',', ' ')\
                .replace('.', ' ')\
                .replace(':', ' ')\
                .replace(';', ' ')\
                .replace('\"', ' ')
        self.corpus_data = [w for w in word_tokenize(data_en)]
        # print(txtfiltered)
        # print(len(txtfiltered))

    def get_data(self):
        return self.corpus_data


if __name__ == '__main__':
    aa = Corpus('leipzig_indonesia.txt')
    print(aa.get_data())