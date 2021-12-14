import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve, generate_binary_structure
import os.path


'''
Moin, 

hab jetzt leider noch keinen Plot für die Temperaturveränderung gemacht, 
aber wenn man das so durchlaufen lässt wie weiter unten, dann lässt sich da ein Phasenübergang erkennen. 


Der liegt bei mir irgendwo 0.8 < T_C < 1.2 oder so. 



'''


J = 1

magn = []
N = 10
iterations = 1000
anfangs_bedingung = 0.5        # gibt an wie viele der initial Spins +1 bzw. -1 sind
inverse_temperatur = 0

inverse_temperatur_array = np.arange(0, 5, 0.2)



def mach_flip(N, anfangs_bedingung, iterations, inverse_temperatur):
    
    energies = np.zeros(iterations)
    spins = np.zeros(iterations)
    

    kernel = np.array([[False, True, False], [True, False, True], [False, True, False]])

    ### initial conditions

    magnet = np.random.random([N,N])
    magnet[magnet > anfangs_bedingung] = 1
    magnet[magnet <= anfangs_bedingung] = -1


    #### interaktiver Plot
    normie = plt.Normalize(vmin=-1, vmax=1)
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_axis_off()

    im = ax.imshow(magnet, cmap='binary', norm=normie )

    ####

    for ii in range(0,iterations):

        spec_energy =  np.sum(  magnet * convolve(magnet, kernel, mode='wrap'))

        spec_spin = np.sum(magnet)


        wo = np.random.randint([N,N])


        
        mom_spin =  magnet[wo[0],wo[1]]

        # beachte periodische Randbedingungen
        
        nachbars =  0 
        
        if wo[0] == 0:
            nachbars += magnet[wo[0]+1, wo[1]]
            nachbars += magnet[-1, wo[1]] 
        elif wo[0] == N-1:
            nachbars += magnet[0, wo[1]]
            nachbars += magnet[wo[0]-1, wo[1]] 
        else: 
            nachbars +=  magnet[wo[0]+1, wo[1]] 
            nachbars +=  magnet[wo[0]-1,wo[1]] 

        
        if wo[1] == 0:
            nachbars += magnet[wo[0], -1] 
            nachbars += magnet[wo[0], wo[1]+1] 
        elif wo[1] == N-1:
            nachbars += magnet[wo[0], wo[1]-1] 
            nachbars += magnet[wo[0], 0]
        else:
            nachbars += magnet[wo[0], wo[1]-1] 
            nachbars += magnet[wo[0], wo[1]+1] 
    
        
        diff_E = nachbars* magnet[wo[0], wo[1]]



        ## WOLFF RAWR

        dump = []
        randy_spin = np.random.randomint(0,N)




        #print(diff_E)
        
        if diff_E <= 0:
            magnet[wo[0], wo[1]] *= -1
        elif diff_E > 0:
            if np.random.random() < np.exp(-inverse_temperatur*diff_E* J):
                magnet[wo[0], wo[1]] *= -1 

        energies[ii] = spec_energy
        spins[ii]  = spec_spin
        im.set_data(magnet)
        fig.canvas.draw()
        fig.canvas.flush_events()
        if ii == iterations-1:
            plt.close()
            plt.ioff()
            
    return energies, spins

'''
for jj in inverse_temperatur_array:
    print(jj)
    energie, spins = mach_flip(N, anfangs_bedingung, iterations, jj)
    
    plt.plot(spins)
    plt.show(block=False)
    plt.pause(4)
    plt.close()
'''