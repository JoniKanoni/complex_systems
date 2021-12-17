import numpy as np
import matplotlib.pyplot as plt


xxxx = np.empty([5,5])


def mat2vec(x):
    m = x.shape[0]*x.shape[1]
    tmp1 = np.zeros(m)

    c = 0
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            tmp1[c] = x[i,j]
            c +=1
    return tmp1


print(xxxx)
print(mat2vec(xxxx))