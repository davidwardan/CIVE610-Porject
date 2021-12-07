# import libraries
from truss_element_stiffness import truss_element_stiffness
import numpy as np
from truss_data_input import *

def truss_global_stiffness(COORD, MPRP, EM, CP):

    # get shape of coordinates matrix    
    num_rows, num_cols = COORD.shape
    
    # retrieve number of nodes and elements from num_rows
    n_nodes = num_rows    

    ndof = n_nodes # number of degrees of freedom
    dof = 2 # each node contains two degrees of freedom

    # get shaoe of global stifness matrix
    N = ndof * dof

    # initiate NxN stiffness matrix with zeros
    glob_k = np.zeros((N,N))

    # itearte over each member in structure
    n_member = np.size(MPRP, 0) 

    # get connections start and end point
    CONNEC = MPRP[:,:2]-1
    
    for i in range(n_member):

        # get member coordinates
        x1 = COORD[CONNEC[i, 0],0]
        y1 = COORD[CONNEC[i, 0],1]

        x2 = COORD[CONNEC[i, 1],0]
        y2 = COORD[CONNEC[i, 1],1]

        # get member modulus of elasticity
        E = EM[i]

        # get member cross section
        A = CP[i]

        # get element stiffness
        k = truss_element_stiffness(x1,y1,x2,y2,E,A)

        # reposition stiffness
        T=np.zeros((4,N))
        T[0 , 2*CONNEC[i, 0]]=1
        T[1 , 2*CONNEC[i, 0]+1]=1
        T[2 , 2*CONNEC[i, 1]]=1
        T[3 , 2*CONNEC[i, 1]+1]=1

        # update global stiffness
        glob_k += np.dot(np.transpose(T),np.dot(k,T))

    return glob_k