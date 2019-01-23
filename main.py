"""
This is the main entrance of our
metaphor recognization system
"""
from util.preprocessing import preprocess_Literary
from LexicalRecognizer import LexicalRecognizer


if __name__ == '__main__':
    dataset = preprocess_Literary('data/literary/metaphor.txt')
    print (dataset)

    word_list = ['是', '似', '如', '像', '比', '好比',
                 '若', '好像', '好似', '仿佛', '有如', '如同']
    recognizer = LexicalRecognizer(word_list)
    predictions = recognizer.recognize(dataset)

    recall = recognizer.recall(dataset, predictions)
    print ("recall: {}".format(recall))
