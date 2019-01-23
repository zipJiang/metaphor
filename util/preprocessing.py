from bs4 import BeautifulSoup
import thulac
import os


class CharacterTokenizer:
    def __init__(self):
        pass

    def tokenize(self, sentence):
        tokens = []
        for char in sentence:
            tokens.append(char)

        return tokens


class ThuLacTokenizer:
    def __init__(self):
        self.tokenizer = thulac.thulac()

    def tokenize(self, sentence):
        with_tag = self.tokenizer.cut(sentence, text=True)

        with_tag_list = with_tag.split(' ')

        tokens = []

        for item in with_tag_list:
            token = item.split('_')[0]
            tokens.append(token)

        return tokens


def preprocess_PSUCMC(directory):
    dir_list = os.listdir(directory)
    for dir_name in dir_list:
        if dir_name[0] == '.':
            continue
        elif dir_name[-4:] == 'docx':
            continue
        full_name = os.path.join(directory, dir_name)
        file_list = os.listdir(full_name)

        # Our recognition is on sentence level


def preprocess_Literary(filename):
    metaphor_file = open(filename, 'r')
    tokenizer = ThuLacTokenizer()
    dataset = []

    for line in metaphor_file:
        trimed = line[:-1]

        tokens = tokenizer.tokenize(trimed)

        flag = 1

        dataset.append((tokens, flag))

    return dataset


if __name__ == '__main__':
    #  preprocess_PSUCMC('../data/PSUCMC')
    dataset = preprocess_Literary('../data/literary/metaphor.txt')
