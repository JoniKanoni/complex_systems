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

    size= 100
    baum_freq = 5
    fire_freq = 0.05
    timestep = 0.001
    
    immnun = 0

    FIRE_VAL = -1000000             # wenn man verschiedene FIRE_VALs hat könnte man Lawinen die gleichzeitig passieren unterscheiden
                                    # bin ich aber vermutlich nicht smart genug für
    
    forest_fire = np.zeros([size,size])

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()
    im = ax.imshow(forest_fire, cmap=cmap, norm=normie)

    nachbarn = [ [-1,1],[-1,0],[-1,-1],[0,1],[0,-1],[1,1],[1,0],[1,-1] ]    

    avas = []

    for ii in range(0,iterations):
        counter = 0
        wo_feuer = np.argwhere(forest_fire < 0)

        for feufeu in range(0, len(wo_feuer) ):
            counter = counter + len(wo_feuer[0]) 
            posi_feu = wo_feuer[feufeu]
            try:
                for neighbours in range(0, len(nachbarn)-1):
                    stuff = forest_fire[posi_feu[0] + nachbarn[neighbours][0], posi_feu[1] + nachbarn[neighbours][1]]
                    if stuff > 0: 
                        forest_fire[posi_feu[0] + nachbarn[neighbours][0], posi_feu[1] + nachbarn[neighbours][1]]  = FIRE_VAL

            except IndexError:              # ziemlich faul, aber immerhin cooler als Malte ;)
                pass

            forest_fire[posi_feu[0],posi_feu[1]] = 0            #positionen zwischenspeichern?
            
            #forest_fire[posi_feu[0],posi_feu[1]] = 0
        avas.append(counter)  
                
        grid = np.random.random([size,size])
        forest = grid < baum_freq*timestep
        forest = forest.astype(int)
        
        fire = grid < fire_freq*timestep
        fire = FIRE_VAL*fire.astype(int)
        
        forest_fire =  forest_fire +  forest + fire




        #draw next iteration

        im.set_data(forest_fire)
        fig.canvas.draw()
        fig.canvas.flush_events()
        
        ###

    np.savetxt('av.txt', avas)        

    return forest_fire

X = baums()    

'''

log_bins = 30
avas = np.loadtxt('av.txt')
counts, bin_edges = np.histogram(avas, bins=np.logspace(0, np.log10(np.max(avas)), log_bins))
counts = counts/np.diff(bin_edges)



fig, ax = plt.subplots(2,2, figsize=(16,8))

arts = []

ax[1,1].set_yscale('log')
ax[1,1].set_xscale('log')
art = ax[1,1].bar(np.arange(log_bins), np.repeat(0, log_bins), ec='k')
# art = ax[1,1].scatter(np.arange(tmax), np.empty(tmax))
arts.append(art)


counts, bin_edges = np.histogram(avas, bins=np.logspace(0, np.log10(np.max(avas)), log_bins))
counts = counts/np.diff(bin_edges)
bin_centres = np.sqrt(bin_edges[1:]*bin_edges[:-1])
mask = counts==0
for bar, height, width, x in zip(arts[0], counts, np.diff(bin_edges), bin_edges[:-1]):
    bar.set_height(height)
    bar.set_width(width)
    bar.set_x(x)
ax[1,1].set_xlim(0.1,np.max(avas)*1.1)
counts = np.ma.masked_array( counts, mask=mask ).compressed()
bin_centres = np.ma.masked_array( bin_centres, mask=mask ).compressed()


plt.show()
plt.pause(10)
'''
