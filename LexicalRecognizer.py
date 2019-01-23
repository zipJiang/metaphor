"""
This file contains a lexical metaphor detector
"""
from util.Recognizer import Recognizer


class LexicalRecognizer(Recognizer):
    def __init__(self, word_list):
        super(LexicalRecognizer, self).__init__()
        self.word_set = set(word_list)

    def recognize(self, dataset):

        result = []
        for item in dataset:
            sentence = item[0]
            sset = set(sentence)

            if len(sset & self.word_set) > 0:
                result.append(1)
            else:
                result.append(0)

        return result

    def recall(self, dataset, predictions):
        tags = [item[1] for item in dataset]

        assert len(tags) == len(predictions)

        TP = 0
        FN = 0

        for pair in zip(tags, predictions):
            if pair[0] == 1 and pair[1] == 0:
                FN += 1
            elif pair[0] == 1 and pair[1] == 1:
                TP += 1

        return TP / (TP + FN)
