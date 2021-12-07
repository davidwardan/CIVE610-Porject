import numpy as np
from truss_data_input import *

def deformed_COORD(COORD, U):

    deformed_COORD = np.zeros(COORD.shape)

    #U = U*1000 #scale up for plotting

    r=0
    for i in range(int(len(U)/2)):
        c=0
        deformed_COORD[r,c]=U[2*i]
        c+=1
        deformed_COORD[r,c]=U[(2*i)+1]
        r +=1

    deformed_COORD += COORD

    return deformed_COORD

        

    

