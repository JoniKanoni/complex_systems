import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap


def baums():
    '''
    Puts Bäume on a grid
    
    Hatte Lust das mit einem Poisson-Prozess zu machen...
    '''

    plt.ion()
    cmap = plt.cm.RdYlGn 
    normie = plt.Normalize(vmin=-1, vmax=1)




    iterations = 10000

    size=100
    baum_freq = 5
    fire_freq = 0.01
    timestep = 0.001
    

    
    forest_fire = np.zeros([size,size])

    fig = plt.figure(figsize=(25/3, 6.25))
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    im = ax.imshow(forest_fire, cmap=cmap, norm=normie)



    for ii in range(0,iterations):
        grid = np.random.random([size,size])
        forest = grid < baum_freq*timestep
        forest = forest.astype(int)

    
        #fire = np.random.random([size,size])
        fire = grid < fire_freq*timestep
        fire = -1000000*fire.astype(int)
        im.set_data(forest_fire)
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        forest_fire =  forest_fire +  forest + fire




    '''
    for ii in forest_fire:
        if ii 
    '''  

    return forest_fire

X = baums()    

'''
cmap = plt.cm.RdYlGn 
normie = plt.Normalize(vmin=-1, vmax=1)

#plt.imshow(X, cmap=cmap, norm=normie)
#plt.show()

#X = np.zeros([1000,1000])



fig = plt.figure(figsize=(25/3, 6.25))
ax = fig.add_subplot(111)
ax.set_axis_off()
im = ax.imshow(X, cmap=cmap, norm=normie)




def animate(i):
    im.set_data(animate.X)
    animate.X = baums(animate.X)

animate.X = X

# Interval between frames (ms).
interval = 100
anim = animation.FuncAnimation(fig, animate, interval=interval, frames=200)
plt.show()
'''
