# Will use Sklearn to Generate a DataSet
# Will use matplotlib to Generate a graph of the dataset

#Note There is a lot of uncommented code I left here to show where I was failing to get the PLA to run.
# I believe the way I am generating the dataset may not be linearly seperatble


from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
import numpy as np
import os

ITERATIONS = 100 #Number of Iterations for the PLA
LEARNING_RATE = 1 #Learning Rate for the PLA
DATAPOINTS = 150 #Number of Samples

# Generate a Training DataSet
class DataSet:
    def __init__(self):
        self.data = None
        self.n = DATAPOINTS #number of data points
        self.centers = 2 #number of clusters
        self.features = 2 #number of features

    # Utilize the sklearn.dataset.mank_blobs method to generate a training dataset
    def generate_dataset(self):
        X, y = make_blobs(n_samples=self.n, centers=self.centers, n_features=self.features)
        return X, y

class Preceptron:
    def __init__(self):
        self.dataset = DataSet()
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.weights = None
        self.bias = None
        self.iterations = ITERATIONS
        self.learning_rate = LEARNING_RATE

    # Contructs our dataset. 80/20 Train/Test Model
    def generate_data(self):
        try:
            data = self.dataset.generate_dataset()
            # self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(data[0], data[1], test_size=0.2)
            self.X_train = np.array([
                                        [-2,4,-1],
                                        [4,1,-1],
                                        [1, 6, -1],
                                        [2, 4, -1],
                                        [6, 2, -1],
                                        [3, 8, -1],
                                        [-1, 4, -1],
                                        [-3, 2, -1],
                                        [5, 1, -1],
                                        [1, 1, -1]
                                    ])
            self.y_train = np.array([-1,-1,1,1,1, 1, -1, -1, -1, -1])
        except Exception as e:
            print(f"Error - Failed to generate a dataset.\n{str(e)}")
            return False

    # Sets our output to either 1 or 0. 1-Correct, 0-Incorrect Iterating through the arrary
    # def evaluate(self, prediction):
    #     return np.where(prediction >= 0, 1, 0)

    # def predictions(self):
    #     raw_prediction = np.dot(self.X_test, self.weights) + self.bias
    #     predicted_y = self.evaluate(raw_prediction)
    #     return predicted_y

    def pla_train(self):
        if self.generate_data() is False:
            return False

        num_samples, num_features = self.X_train.shape
        self.weights = np.zeros(len(self.X_train[0]))
        print(f"Initial weights::{self.weights}")
        self.bias = 1
        missclassified = []

        for iter in range(self.iterations):
            errors = 0
            for i, xi in enumerate(self.X_train):

                if (np.dot(self.X_train[i], self.weights)*self.y_train[i]) <= 0:
                    errors += (np.dot(self.X_train[i], self.weights) * self.y_train[i])
                    self.weights = self.weights + self.bias * self.X_train[i] * self.y_train[i]
                missclassified.append(errors*-1)

        print(f"Calculated weights::{self.weights}")
        print("Displaying graph of iterations throught PLA...")

        plt.plot(missclassified)
        plt.xlabel("Iterations")
        plt.ylabel("Total Misclassifications")
        plt.show()
        return True

    def pla_test(self):
        pass

def main():
    p = Preceptron()
    if p.pla_train() is False:
        print("Failed to train the data set")
        os._exit(1)
    # if p.pla_test() is False:
    #     print("Failed to test the PLA")
    #     os._exit(0)
    print("Done!")

if __name__ == '__main__':
    main()
