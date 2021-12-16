import numpy as np
import matplotlib.pyplot as plt


N = 32
def make_pat(n):
    '''
    Macht 3 binäre Muster
    '''
    
    np.random.seed(1234)
    pat1 = np.reshape(np.random.randint(2, size=n**2) ,  (n,n))
    pat1 = np.where(pat1==0, -1, pat1)

    np.random.seed(4321)
    pat2 = np.reshape(np.random.randint(2, size=n**2) ,  (n,n))
    pat2 = np.where(pat2==0, -1 , pat2)

    np.random.seed(7777)
    pat3 = np.reshape(np.random.randint(2, size=n**2) ,  (n,n))
    pat3 = np.where(pat3==0, -1, pat3)
    return pat1, pat2, pat3
p1, p2, p3 =  make_pat(N)

all = (p1,p2,p3)

def weights(n, patterns):
    '''
    initial weights
    56 connections ungleich 0 bei N=8, da keine Kopplung mit sich selbst aka Diagonale=0
    '''   
    w_init = np.zeros((n,n)) 

    # matrixmultiplikation und so für die weights
    for x in patterns:
        w_init +=  np.outer(x[0], x[0]) / n    
    np.fill_diagonal(w_init, 0)     #W_ii = 0

    return w_init

w = weights(N, all)

print(np.shape(w))

bias = np.sum(all, axis=0) / len(all)
print(np.shape(bias))
def energy(patterns, W):
    '''
    Energie.. falls man asynchron sein will
    '''
    Energy = []
    for x in patterns:
        hmm = -1/2 * np.matmul(x, W)
        Energy.append(hmm)

    return Energy

e = energy(all, w)

def breaker(pat):
    '''
    random noise auf pattern.
    Ich sage, dass shufflen und randomly multiplizieren der Punkte mit +-1 genau das "gleiche" Resultat ergeben
    '''
    pp = np.copy(pat)
    np.random.shuffle(pp)
    return pp
pag = breaker(p2)

def recaller(inp, W,  iterations, bias):
    '''
    Vergleicht und updatet
    '''
    hmm = inp
    for ii in range(iterations):
        new_pos = np.matmul(hmm, W) 
        hmm = np.sign(new_pos)
    return hmm

membered = recaller(p2, w, 100000, bias)

plt.subplot(311)
plt.ylabel('original')
plt.legend(str(np.sum(p2)))
plt.imshow(p2)
plt.subplot(312)
plt.ylabel('scuffed')
plt.legend(str(np.sum(pag)))
plt.imshow(pag)
plt.subplot(313)
plt.ylabel('remembered')
plt.legend(str(np.sum(membered)))
plt.imshow(membered)

plt.show()
