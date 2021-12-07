# import libraries
import numpy as np

def get_plot_COORD(COORD, MPRP):

    lst=[]
    for row in MPRP:
        lst.append(COORD[row[0]-1])
        lst.append(COORD[row[1]-1])

    return np.array(lst)
        

