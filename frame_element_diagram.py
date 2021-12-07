import numpy as np
import math
from frame_plot import plot_MDR
from frame_element_stifness import frame_element_stifness
from frame_transform import transform

def frame_elemt_diagram(COORD, MPRP, EM, CP, IP, P, M ,W , F, U, Th, Delta, MR):

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

        #calcualte length of member
        L = math.sqrt((x2-x1)**2+(y2-y1)**2)

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

        # get F and U of member
        MEMB = CONNEC[i]

        U_ = []
        for l in  MEMB:
            U_.append(float(U[3*l]))
            U_.append(float(U[3*l+1]))
            U_.append(float(U[3*l+2]))

        U_ = np.transpose(np.array([U_]))

        # get element stiffness matrix
        k , pf = frame_element_stifness(x1,y1,x2,y2,E,A,I, p, m, w ,th , delta , mr)

        F_ = np.dot(k,U_) + pf

        R_ = []
        for f in F_:
            R_.append(f[0])

        _, _, t = transform(x1, y1, x2, y2, k, pf)

        U_ = np.dot(t,U_)

        # plot diagrams of each member
        R1=F_[1]
        M1=F_[2]
        v1=U_[1]
        r1=U_[2]

        R2=F_[4]
        M2=F_[5]
        v2=U_[4]
        r2=U_[5]
        
        plot_MDR(R1, M1, v1 ,r1,R2, M2, v2 ,r2, L, p[0], p[1] , m[0] ,m[1], w[2] ,E ,I)
        
