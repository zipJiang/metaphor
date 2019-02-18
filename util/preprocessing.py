from bs4 import BeautifulSoup
import thulac
import os
import re
import random


class SentenceTokenizer:
    def __init__(self):
        pass

    def tokenize(self, paragraph):
        # paragraph should be a string with sentences
        result = re.findall(u'[^。？！”；：]*[。？！”；：]', paragraph)
        return result


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
        # TODO: To further simplify this dataset


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


def preprocess_THUsamples(thu_loc, catname=None):
    # First we have to tokenize sentence
    if catname is None:
        categories = os.listdir(thu_loc)
    else:
        assert catname in categories
        categories = [catename]

    jumpover = '　'

    sent_tokenizer = SentenceTokenizer()
    tokenizer = ThuLacTokenizer()

    all_sentences = []
    for category in categories:
        print ('processing category: {}'.format(category))
        cat_loc = os.path.join(thu_loc, category)
        for filename in os.listdir(cat_loc):
            # filter the filename
            if filename[0] == '.':
                continue
            file_loc = os.path.join(cat_loc, filename)

            # read that file
            current_file = open(file_loc, 'r')
            for line in current_file:
                # filter the line
                while line[0] == jumpover:
                    line = line[1:]
                if len(line) == 1:
                    continue
                sentences = sent_tokenizer.tokenize(line[:-1])
                # for convenience we are adding a 1
                # label to all the sentences
                label = 1
                for sent in sentences:
                    st_list = tokenizer.tokenize(sent)
                    all_sentences.append((st_list, label))

    return all_sentences


if __name__ == '__main__':
    preprocess_THUsamples('../data/THUsamples')
