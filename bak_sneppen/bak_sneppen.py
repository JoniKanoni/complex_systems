import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


species = 100
iterations = 10

fitness = np.random.random([species])
lambo = 0.6

counter = 0

ava_length = []

for ii in range(0,iterations):
       
    minimum = np.min(fitness) 
    if minimum < lambo:
        counter = counter +1        # +1 für jeden Zeitschritt der Lawine
        fitness_binary = fitness < lambo
        fitness_binary.astype(int) 
        ava_size = np.sum(fitness_binary)
    elif minimum > lambo:
        ava_length.append(counter)
        counter = 0
    minimum_pos = np.where(fitness ==  minimum)[0][0]

    fitness[minimum_pos] = np.random.random(1)

    if minimum_pos == 0:
        neighbour_links = species-1
        neighbour_rechts = minimum_pos+1
    elif minimum_pos == species-1:
        neighbour_rechts = 0 
        neighbour_links = minimum_pos-1
    else: 
        neighbour_links = minimum_pos-1 
        neighbour_rechts = minimum_pos+1
    fitness[neighbour_links] = np.random.random(1)    
    fitness[neighbour_rechts] =np.random.random(1)
    if ii == iterations-1:
        print(np.mean(fitness))
        plt.scatter( np.arange(len(fitness)), fitness)
        plt.hlines(2/3, 0, len(fitness), color='r')
        plt.hlines(lambo, 0, len(fitness), color='g')
        plt.show()

np.savetxt('ava_length.txt', ava_length)