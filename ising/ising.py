import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve, generate_binary_structure





N = 20

anfangs_bedingung = 0.1

iterations = 10000

energies = np.zeros(iterations)
spins = np.zeros(iterations)


kernel = np.array([[False, True, False], [True, False, True], [False, True, False]])

inverse_temperatur = np.inf
     #quasi temp


### initial conditions

magnet = np.random.random([N,N])
magnet[magnet > anfangs_bedingung] = 1
magnet[magnet <= anfangs_bedingung] = -1


#### interaktiver Plot

plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axis_off()

im = ax.imshow(magnet, cmap='binary')

####

for ii in range(0,iterations):

    spec_energy =  np.sum(  magnet * convolve(magnet, kernel))

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



    #print(diff_E)
    
    
    flipper = float(np.exp(-inverse_temperatur*diff_E))
    if diff_E <= 0:
        magnet[wo[0], wo[1]] *= -1
    elif np.random.random() < flipper:
        magnet[wo[0], wo[1]] *= -1 

    energies[ii] = spec_energy
    spins[ii]  = spec_spin
    im.set_data(magnet)
    fig.canvas.draw()
    fig.canvas.flush_events()
#print(energies)



