import numpy as np
import matplotlib.pyplot as plt
import copy


def make_pat(n):
    '''
    Macht 3 binäre Muster als Vektor
    Seeds kann man enablen um die reproduzierbarkeit zu checken, ist aber die doofe Version der Seeds.. 
    Deswegen lieber ausmachen, weil diese Art von Seeds dann doch manchmal global sind und das Shufflen hinten beeinflussen können..
    Idk nunmp
    
    '''
    
    #np.random.seed(1234)
    pat1 = np.random.randint(2, size=n**2) 
    pat1 = np.where(pat1==0, -1, pat1)

    #np.random.seed(4321)
    pat2 = np.random.randint(2, size=n**2)
    pat2 = np.where(pat2==0, -1 , pat2)

    #np.random.seed(7777)
    pat3 = np.random.randint(2, size=n**2)
    pat3 = np.where(pat3==0, -1, pat3)
    return pat1, pat2, pat3

def weights(n, patterns):
    '''
    initial weights
    56 connections ungleich 0 bei N=8, da keine Kopplung mit sich selbst aka Diagonale=0
    '''   
    w_init = np.zeros((64,64)) 

    # matrixmultiplikation und so für die weights
    
    for x in patterns:
        w_init +=     np.outer(x,x)  #np.matmul(x, x)     #np.dot(x, x) / n    
    np.fill_diagonal(w_init, 0)     #W_ii = 0
    
    return w_init

def breaker(pat):
    '''
    random noise auf pattern.
    Ich sage, dass shufflen und randomly multiplizieren der Punkte mit +-1 genau das "gleiche" Resultat ergeben
    '''
    pp = np.copy(pat)
    np.random.shuffle(pp)
    return pp

def recaller(inp, W,  iterations, bias):
    '''
    Vergleicht und updatet
    hmm braucht man eigentlich nicht, aber ich habs ein bisschen zu meiner eigenen Sicherheit eingeführt
    '''
    hmm = inp
    for ii in range(iterations):
        new_pos = -np.matmul(hmm, W)  -bias 
        hmm = -np.sign(new_pos)
    return hmm

N = 8

p1, p2, p3 =  make_pat(N)

all = (p1,p2,p3)

w = weights(N, all)

bias = np.sum(all, axis=0) / len(all)

pag = breaker(p1)

membered = recaller(pag, w, 10, bias)

# hier nur reshape damit schönere Plots
p1 = np.reshape(p1, (N,N))
p2 = np.reshape(p2, (N,N))
p3 = np.reshape(p3, (N,N))
pag = np.reshape(pag, (N,N))
membered = np.reshape(membered, (N,N))


# plots
fig, axs = plt.subplots(2,3, constrained_layout=True)

axs[0,0].imshow(p1)
axs[0,0].set_ylabel('Pattern 1')
axs[0,0].tick_params(axis='both', length=0, width=0, labelsize=0)
axs[0,1].imshow(p2)
axs[0,1].set_ylabel('Pattern 2')
axs[0,1].tick_params(axis='both', length=0, width=0, labelsize=0)
axs[0,2].imshow(p3)
axs[0,2].set_ylabel('Pattern 3')
axs[0,2].tick_params(axis='both', length=0, width=0, labelsize=0)

axs[1,0].imshow(w)
axs[1,0].set_ylabel('Weights')
axs[1,0].tick_params(axis='both', length=0, width=0, labelsize=0)

axs[1,1].imshow(pag)
axs[1,1].set_ylabel('Input Pattern')
axs[1,1].tick_params(axis='both', length=0, width=0, labelsize=0)

axs[1,2].imshow(membered)
axs[1,2].set_ylabel('Remembered Pattern')
axs[1,2].tick_params(axis='both', length=0, width=0, labelsize=0)


plt.show()
