class Recognizer:
    def __init__(self):
        pass

    def recognize(dataset):
        result = []
        return result

    def accuracy(dataset, predictions):
        tags = [item[1] for item in dataset]

        assert len(tags) == len(predictions)

        correct = 0

        for instance in zip(tags, predictions):
            if instance[0] == instance[1]:
                correct += 1

        return correct / len(tags)
