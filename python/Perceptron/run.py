# Will use Sklearn to Generate a DataSet
# Will use matplotlib to Generate a graph of the dataset
from sklearn.datasets import make_blobs
from matplotlib import pyplot as plot
import numpy as np
import os

class DataSet:
    def __init__(self):
        self.data = None
        self.n = 100 #number of data points
        self.centers = 2 #number of clusters
        self.features = 2 #number of features

    def generate_data(self):
        X, y = make_blobs(self.n, self.centers, self.features)
        return X, y

class Preceptron:
    def __init__(self):
        self.dataset = Dataset()
        self.X = None
        self.y = None
        self.weights = None
        self.bias = None

    def generate_data(self):
        try:
            data = self.dataset.generate_data()
            self.X = data[0]
            self.y = data[1]
        except Exception as e:
            print(f"Error - Failed to generate a dataset.\n{str(e)}")
            return False

    # Sets our output to either 1 or 0. 1-Correct, 0-Incorrect
    def evaluate(self, prediction):
        if prediction >= 0:
            return 1
        return 0

    def predict(self):
        raw_prediction = np.dot(self.X, self.weights) + self.bias
        predicted_y = self.evaluate(raw_prediction)
        return predicted_y

    def fit(self):
        if self.initialize() is False:
            return False

        num_samples, num_features = X.shape
        self.weights = np.zeros(num_features)
        self.bias = 0

        return True

def main():
    p = Preceptron()
    if p.fit() is False:
        print("Failed to start project")
        os._exit(1)

if __name__ == '__main__':
    main()
