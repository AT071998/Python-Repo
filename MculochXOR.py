import numpy as np
import pandas as pd

class Neuron:

    def __init__(self, weight , threshold):
        self.weight = np.array(weight);
        print("Weights Given is:",self.weight)
        self.threshold = threshold

    def compute(self , message):
        x_msg = message;
        sum = np.inner(self.weight, x_msg)
        print("sum of", x_msg, "is", sum);
        if sum >= self.threshold:
            return 1
        else:
            return 0


    def TruthTable(self, input_signals, input_labels, output_label):
        table = pd.DataFrame(input_signals, columns=input_labels)

        output_signals = []
        for row in input_signals:
            signal = self.compute(message=row)
            output_signals.append(signal)
            table[output_label] = pd.Series(output_signals)
        return table


input_signals = np.array([[0, 0], [1, 0], [0, 1], [0, 0]])
input_labels = ['x1', 'x2']
output_labels = 'y'
OR = Neuron([3, 3], 3)

OR_Table = OR.TruthTable(input_signals, input_labels=input_labels, output_label=output_labels)
print("**Displaying Truth Table of OR Gate")
print(OR_Table)