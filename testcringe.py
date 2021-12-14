import numpy as np
import matplotlib.pyplot as plt

N = 10

anfangs_bedingung = 0.5

magnet = np.random.random([N,N])
magnet[magnet > anfangs_bedingung] = 1
magnet[magnet <= anfangs_bedingung] = -1


def nachbar_sucht_spin(wo, ):
    '''
    sorry für die Variablennamen..
    '''
    nachbars  = 0
    dump = np.array([])
    if wo[0] == 0:
        GLGL  = magnet[wo[0]+1, wo[1]]
        glgl  = magnet[-1, wo[1]]

        nachbars += GLGL
        nachbars += glgl

        if glgl == magnet[wo[0], wo[1]]:
            dumn =  np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)
    elif wo[0] == N-1:  

        GLGL  = magnet[0, wo[1]]
        glgl  = magnet[wo[0]-1, wo[1]]

        nachbars += GLGL
        nachbars += glgl

        if glgl == magnet[wo[0], wo[1]]:
            dump =  np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)

    else: 
        glgl = magnet[wo[0]+1, wo[1]] 
        GLGL = magnet[wo[0]-1,wo[1]]
        nachbars +=  glgl 
        nachbars +=   GLGL

        if glgl == magnet[wo[0], wo[1]]:
            dump = np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)
        
    if wo[1] == 0:

        glgl = magnet[wo[0], -1]   
        GLGL = magnet[wo[0], wo[1]+1] 

        nachbars +=  glgl
        nachbars += GLGL

        if glgl == magnet[wo[0], wo[1]]:
            dump = np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)

    elif wo[1] == N-1:

        glgl = magnet[wo[0], wo[1]-1] 
        GLGL = magnet[wo[0], 0]

        nachbars += glgl
        nachbars += GLGL

        if glgl == magnet[wo[0], wo[1]]:
            dump = np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)
    else:
        
        glgl = magnet[wo[0], wo[1]-1]
        GLGL  =  magnet[wo[0], wo[1]+1] 
        nachbars +=  glgl

        nachbars += GLGL

        if glgl == magnet[wo[0], wo[1]]:
            dump =  np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)   
    
    
    return dump, alle






wo = np.random.randint(0,N,  size=2)
dump = np.array([wo])

lol, alle = nachbar_sucht_spin(wo)
print(lol)
'''
plt.imshow(magnet)
plt.show()

for xx in range(0,1000):
    #check neighbours
    if wo[0] == 0:
        GLGL  = magnet[wo[0]+1, wo[1]]
        glgl  = magnet[-1, wo[1]]

        
        

        nachbars += GLGL
        nachbars += glgl

        if glgl == magnet[wo[0], wo[1]]:
            dumn =  np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)
    elif wo[0] == N-1:  

        GLGL  = magnet[0, wo[1]]
        glgl  = magnet[wo[0]-1, wo[1]]

        
        nachbars += GLGL
        nachbars += glgl

        if glgl == magnet[wo[0], wo[1]]:
            dump =  np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)

    else: 
        glgl = magnet[wo[0]+1, wo[1]] 
        GLGL = magnet[wo[0]-1,wo[1]]
        nachbars +=  glgl 
        nachbars +=   GLGL

        if glgl == magnet[wo[0], wo[1]]:
            dump = np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)


    
    if wo[1] == 0:

        glgl = magnet[wo[0], -1]   
        GLGL = magnet[wo[0], wo[1]+1] 



        nachbars +=  glgl
        nachbars += GLGL


        if glgl == magnet[wo[0], wo[1]]:
            dump = np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)

    elif wo[1] == N-1:

        glgl = magnet[wo[0], wo[1]-1] 
        GLGL = magnet[wo[0], 0]

        nachbars += glgl
        nachbars += GLGL

        if glgl == magnet[wo[0], wo[1]]:
            dump = np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)
    else:
        
        glgl = magnet[wo[0], wo[1]-1]
        GLGL  =  magnet[wo[0], wo[1]+1] 
        nachbars +=  glgl

        nachbars += GLGL

        if glgl == magnet[wo[0], wo[1]]:
            dump =  np.append(dump, glgl)
        if GLGL == magnet[wo[0], wo[1]]:
            dump = np.append(dump, GLGL)       


#print(magnet[wo[0]  , wo[1]])
#print(nachbars)
print(dump)


#while len(wo) > 0:
'''