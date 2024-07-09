import numpy as np

X = np.array([[1, 2, 3], [5, 8, 10], [20, 0, 3], [1, 5, 8]])
Y = np.array([[6], [13], [23], [14]], dtype='float64')
X_t = X.transpose()

XX_t = np.linalg.inv(X_t @ X)
print(XX_t)
co = XX_t @ X_t @ Y
print(co)