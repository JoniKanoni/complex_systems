import numpy as np
import matplotlib.pyplot as plt



def make_pat():
    '''
    Macht 3 binäre Muster
    '''
    
    N = 64
    n = int( np.sqrt(N))


    np.random.seed(1234)
    pat1 = np.reshape(np.random.randint(2, size=N) ,  (n,n))

    np.random.seed(12345)
    pat2 = np.reshape(np.random.randint(2, size=N) ,  (n,n))

    np.random.seed(123456)
    pat3 = np.reshape(np.random.randint(2, size=N) ,  (n,n))
    return pat1, pat2, pat3
p1, p2, p3 =  make_pat()

plt.imshow(p3)
plt.show()