# pylint: disable=R1728

"""Module containing the Perceptron class and associated functions"""

class Perceptron:
    """Class representing a Perceptron"""
    def __init__(self):
        self._weights = 0
    def train(self, inputs, labels):
        """Function training with dummy inputs"""
        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for entered, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(entered)
                for index, iter_x in enumerate(entered):
                    self._weights[index] += .1 * iter_x * label_delta
    def predict(self, entered):
        """Function predicting with entered parameters"""
        if len(entered) == 0:
            return None
        entered = entered + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, entered)]))
