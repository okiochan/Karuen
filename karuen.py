import numpy as np
import matplotlib.pyplot as plt

def floatfmt(x):
    if(abs(x) < 1e-4): x=0.
    return "{:8.3}".format(x)
np.set_printoptions(formatter={'float': floatfmt })


def display_data(X):
    # return
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_aspect(1)
    ax.scatter(X[:,0],X[:,1],s=10, color='orange')
    plt.show()

# karuening
def karuen(X, eps=1E-15):
    l = X.shape[0]
    X = X-X.mean(axis=0)
    Xcov = np.dot(X.T,X)/l
    d, V = np.linalg.eigh(Xcov)
    D = np.diag(1. / np.sqrt(d+eps))
    W = np.dot(D,V.T)
    X_karuen = X.dot(W.T)
    return X_karuen, d, V

np.random.seed(271828182)
X = np.random.randn(1000,2)
A = np.array([
    [10.0, 8.0],
    [8.0, 4.0]
])
X = X.dot(A)
display_data(X)

X_karuen, d, V = karuen(X)
print(X_karuen)
print()
print(np.dot(X_karuen.T,X_karuen)/X.shape[0]) # [[1,0],[0,1]]
print( X_karuen.mean(axis=0) ) # [0,0]
print( X_karuen.std(axis=0) ) # [1,1]
display_data(X_karuen)