import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
from numpy.linalg import norm

class DataFactory:
    def create(name):
        if name == "iris":
            iris = datasets.load_iris()
            X = iris.data
            y = iris.target
            return X,y
        else:
            raise Exception("Unknown data")

def SingularDecomposition(X):
    l = X.shape[0]
    n = X.shape[1]
    X_cov = np.dot(X.T,X)/l
    D, V = np.linalg.eigh(X_cov)
    reverse = n - 1 - np.arange(n)
    return D[reverse], V[:,reverse]

def Proj(v,u):
    return v.dot(u) / u.dot(u) * u

def EigenDecomposition(A, eps=1e-8):
    n = A.shape[0]

    vectors = []
    values = []
    iterations = 0
    for v in range(n):
        now = np.random.randn(n)
        while True:
            iterations += 1

            # gram schmidt
            for v in vectors:
                now -= Proj(now, v)
            now = now / norm(now)

            nxt = A.dot(now)
            length = norm(nxt)
            nxt = nxt / length
            if np.sum(np.abs(now - nxt)) <= eps:
                vectors.append(nxt)
                values.append(length)
                break
            now = nxt
    print("Iterations taken: ", iterations)
    return np.array(values), np.array(vectors).T


def PrincipalComponents(X, V, count):
    return X.dot(V)[:,np.arange(count)]

def Normalize(X):
    X = X-X.mean(axis=0)
    return X

def RestoreOriginal(X, V):
    n = V.shape[1]
    m = X.shape[1]
    l = X.shape[0]
    zeros = np.zeros((l, n-m))
    X = np.hstack((X,zeros))
    return X.dot(V.T)

def Error(X, count):
    X_hat = PrincipalComponents(X, V, count)
    X_restored = RestoreOriginal(X_hat, V)
    return np.sum((X - X_restored) ** 2)/ X.shape[0] / X.shape[1]

X, y = DataFactory.create("iris")
X = Normalize(X)
D, V = SingularDecomposition(X)

# D1, V1 = EigenDecomposition(np.dot(X.T,X) / X.shape[0])
# print(D)
# print(D1)
# print(D - D1)
# print()
# print(V)
# print(V1)
# print(V / V1)
# print()
# quit()

errors = []
for i in range(X.shape[1]):
    errors.append(Error(X, i+1))

X_two = PrincipalComponents(X, V, 2)

fig, axes = plt.subplots(3)
axes[0].set_title("Eigen Values")
axes[1].set_title("Errors on restore")
axes[2].set_title("Two components")
axes[0].plot(D)
axes[1].plot(errors)
axes[2].scatter(X_two[:,0], X_two[:,1], c=y)
plt.show()

