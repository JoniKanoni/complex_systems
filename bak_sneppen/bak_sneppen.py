import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def evolution(iterations):
    species = 100
    #iterations = 10000

    fitness = np.random.random([species])
    lambo = 0.6                     # Grenze für Lawinenbeginn

    counter = 0                     # counter zählt die Lawinenlänge(dauer)

    ava_length = [] 
    beteiligte = []                 # zählt wie viele Spezies an der Lawine ingsgesamt beteiligt waren
    ava_dump = []                   # Zwischenspeicher für die Beteiligten

    for ii in range(0,iterations):
        
        minimum = np.min(fitness) 
        if minimum < lambo:
            counter = counter +1        # +1 für jeden Zeitschritt der Lawine
            fitness_binary = fitness < lambo
            fitness_binary.astype(int) 
            ava_size = np.sum(fitness_binary)
            ava_dump.append(ava_size)
        elif minimum > lambo:
            ava_length.append(counter)
            beteiligte.append(np.sum(ava_dump))
            ava_dump = []
            counter = 0
        minimum_pos = np.where(fitness ==  minimum)[0][0]

        fitness[minimum_pos] = np.random.random(1)


        # die ifs sorgen dafür, dass falls nebenan kein Nachbar mehr ist (Spezies 100 hat ja keinen rechten Nachbar) 
        # die Spezies am anderen Ende gewählt wird
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
            #print(np.mean(fitness))
            plt.scatter( np.arange(len(fitness)), fitness)
            plt.hlines(2/3, 0, len(fitness), color='r')
            plt.hlines(lambo, 0, len(fitness), color='g')
            plt.ylim((0,1))
            plt.savefig('bak_sneppen.png')
            plt.clf()
    
    #np.savetxt('ava_length.txt', ava_length)
    return beteiligte, ava_length

def plots():
    ''' 
    Führt evolution() durch.
    Macht plots.
    
    Histogram und Lawinengröße gegen Lawinendauer aufgetragen.
    '''
    bet, aval =   evolution(100000)
    #aval = np.loadtxt('ava_length.txt')

    '''
    Die nächsten zwei Zeilen sollten mir die Lawinendauern von 0 rausfiltern, die entstehen wenn sich zwei Zeitschritte hintereinander 
    kein Dot unter dem Lambda befindet. Filtern wurde gemacht damit das mit dem log nicht komisch wird,   .......
    aber das mit dem logarithmischen Histogram ist irgendwie trotzdem komisch geworden. 
    
    Im Ordner befindet sich log und nicht-log Histogram.

    Vielleicht ist es sinnvoll die sehr kleinen Lawinen zu ignorieren (?)...
    '''
    sortiert =     np.sort(  aval[1:len(aval)]    ) # remove hier die erste lawinendauer, weil die ja von einem komplett zufälligen ausgangspunkt beginnt
    relevante_avalanches = sortiert[len(sortiert)-len(np.nonzero(sortiert)[0]):len(sortiert)      ]

    plt.hist(np.log(relevante_avalanches), bins='auto')
    plt.ylabel('Häufigkeit')
    plt.xlabel('Lawinengröße')
    plt.savefig('Histo.png')
    plt.clf()
    #plt.plot(np.log(np.arange(len(sortiert))), np.log(sortiert))    # plottet  log(Lawinendauer)         
    #plt.show()
    plt.scatter(np.log(bet), np.log(aval))
    plt.ylabel('log(Beteiligte Spezies pro Lawine)')
    plt.xlabel('log(Lawinengröße (Dauer))')
    plt.savefig('Lawinensize_dauer.png')

#evolution()
#plots()
