import numpy as np
import matplotlib.pyplot as plt



def baums():
    '''
    Puts Bäume on a grid
    
    Hatte Lust das mit einem Poisson-Prozess zu machen...
    '''
    baum_freq = 5
    fire_freq = 0.1
    timestep = 0.001
    forest = np.random.random([100,100])
    forest = forest < baum_freq*timestep
    forest = forest.astype(int)


    fire = np.random.random([100,100])
    fire = fire < fire_freq*timestep
    fire = -1*fire.astype(int)

    forest_fire = forest + fire
    plt.imshow(forest_fire)
    plt.show()

    '''
    for ii in forest_fire:
        if ii 
    '''    
baums()    




