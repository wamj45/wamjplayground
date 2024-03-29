import numpy as np
import random
from random import randint
import matplotlib.pyplot as plt

class Perceptron:

    def __init__(self, N):
        #random.seed(0)
        self.N = N
        #set a random line by x_a,y_a,x_b,y_b to divide the data into two categories
        x_a,y_a,x_b,y_b = [random.uniform(-1, 1) for i in range(4)]
        w2 = 1 / (x_b * y_a - x_a * y_b)
        w1 = -1 * (y_a - y_b) / (x_a - x_b) * w2
        #weight
        self.W = np.array([1, w1, w2])
        #generate random data points
        self.X = self.generate_data()
        #label random data points by the random line
        self.labels = np.sign(self.W.dot(self.X))

    def generate_data(self):
        #random.seed(0)
        X = np.empty([3,self.N])
        for n in range(self.N):
            x1, x2 = [random.uniform(-1, 1) for i in range(2)]
            X[0][n] = 1
            X[1][n] = x1
            X[2][n] = x2
        return X
    def plot(self):
        x = np.arange(-1.,1.1,0.1)
        y = -1*(1+self.W[1]*x)/self.W[2]
        plt.figure(figsize=(5,5))
        plt.xlim(-1,1)
        plt.ylim(-1,1)
        plt.xlabel('x1')
        plt.ylabel('x2')
        plt.plot(x,y)
        i = 0
        while i < self.N:
            if self.labels[i] > 0:
                plt.plot(self.X[1][i],self.X[2][i],'ro')
            else:
                plt.plot(self.X[1][i],self.X[2][i],'bo')
            i+=1
        #plt.savefig('test1.png')
        plt.show()
    def pla(self):
        iteration = 1000
        i = 0
        rand_w = np.array([1.,0.,0.])
        avg_disagreement_p = 0
        while i < iteration:
           #pick a point randomly from all points
            if i == 0:
                rand = randint(0,self.N-1)
                rand_x = self.X[:,rand]
                rand_w += [j * self.labels[rand] for j in rand_x]
            else:
                mis_pts = self.misclassified_pts(rand_w)
                if len( mis_pts ) == 0:
                    print "converged in "+str(i)+" iterations!"
                    break
                rand = randint(0,len(mis_pts)-1)
                rand_x = self.X[:,mis_pts[rand]]
                rand_w += rand_x*self.labels[mis_pts[rand]]
            i+=1
        #return iteration
        return i

    def misclassified_pts(self, rand_w):
        mis_pts = []
        i = 0
        labels_this_run = np.sign(rand_w.dot(self.X))
        while i < self.N:
            if labels_this_run[i] != self.labels[i]:
                #saving the indexes of misclassified pts
                mis_pts.append(i)
            i+=1
        #outputs a set of misclassified points
        return mis_pts
    def disagreement_p(self, rand_w):
        #test disagreement by random 100 points
        random_pt_test = 100
        disagreement = 0
        for i in range(random_pt_test):
            x = np.array([1, random.uniform(-1,1),random.uniform(-1,1)])
            if np.dot(rand_w, x) != np.dot(self.W, x):
                disagreement += 1
        #outputs the probability of disagreement
        return float(disagreement)/float(random_pt_test)


#start PLA
run = 1000
avg_iter = 0
for i in range(run):
    iteration = Perceptron(100).pla()
    avg_iter += iteration
avg_iter = float(avg_iter)/float(run)
print "after 1000 runs, the avg num of iteration is "+str(avg_iter)+"!"
