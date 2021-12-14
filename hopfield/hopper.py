import numpy as np
import matplotlib.pyplot as plt



def make_pat():
    '''
    Macht 3 binäre Muster
    '''
    
    N = 16

    np.random.seed(1234)
    pat1 = np.reshape(np.random.randint(2, size=N) ,  (4,4))

    np.random.seed(12345)
    pat2 = np.reshape(np.random.randint(2, size=N) ,  (4,4))

    np.random.seed(123456)
    pat3 = np.reshape(np.random.randint(2, size=N) ,  (4,4))
    return pat1, pat2, pat3
make_pat()