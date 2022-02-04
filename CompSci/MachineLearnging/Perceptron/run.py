# Generate DataSet
# Will use Sklearn to Generate a DataSet
# Will use matplotlib to Generate a graph of the dataset
from sklearn.datasets import make_blobs
from matplotlib import pyplot
from pandas import DataFrame

class DataSet:
    def __init__(self):
        self.data = None
        self.n = 100 #number of data points
        self.centers = 2 #number of clusters
        self.features = 2 #number of features

    def generate_data(self):
        X, y = make_blobs(self.n, self.centers, self.features)
