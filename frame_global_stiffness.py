import numpy as np
from frame_data_input import Th
from frame_element_stifness import frame_element_stifness
from frame_transform import transform

def frame_global_stiffness(COORD, MPRP, EM, CP, IP, P, M ,W , Th, Delta , MR):

    # get shape of coordinates matrix    
    num_rows, num_cols = COORD.shape

    # retrieve number of nodes and elements from num_rows
    n_nodes = num_rows

    ndof = n_nodes # number of degrees of freedom
    dof = 3 # each node contains two degrees of freedom

    # get shaoe of global stifness matrix
    N = ndof * dof

    # initiate NxN stiffness matrix with zeros
    glob_k = np.zeros((N,N))

    # initiate 1xN fabrcated froces vecotr with zeros
    Ff = np.zeros((N,1))

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
        E = float(EM[i])

        # get member cross section
        A = float(CP[i])

        # get member moment of inertia
        I = float(IP[i])

        # get load data
        p = P[i]
        m = M[i]
        w = W[i]
        th = Th[i]

        # get settlment data
        delta = Delta[i]

        # get moment releases
        mr = MR[i]

        # get element stiffness matrix
        k , pf = frame_element_stifness(x1,y1,x2,y2,E,A,I, p, m, w ,th , delta , mr)

        # apply trasnformation
        k_T, pf, t = transform(x1, y1, x2, y2, k, pf)

        # reposition stiffness
        T=np.zeros((6,N))
        T[0 , 3*CONNEC[i, 0]]=1
        T[1 , 3*CONNEC[i, 0]+1]=1
        T[2 , 3*CONNEC[i, 0]+2]=1
        T[3 , 3*CONNEC[i, 1]]=1
        T[4 , 3*CONNEC[i, 1]+1]=1
        T[5 , 3*CONNEC[i, 1]+2]=1

        # update global stiffness
        glob_k += np.dot(np.transpose(T),np.dot(k_T,T))

        # update fabricated forces
        Ff += np.dot(np.transpose(T), pf)

    return glob_k, Ff
