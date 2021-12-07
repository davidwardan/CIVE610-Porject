import numpy as np
from truss_data_input import *

def truss_f_d(glob_k, kff, kcf, MSUP, PJ, ff, cc):

    # get external forces vector
    F=[]
    
    for row in PJ:
        F.append(row[0])
        F.append(row[1])
    
    F=np.array(F)

    Ff=F[ff] 

    # get flexibility matrix
    d= np.linalg.inv(kff)

    # get displacement vector
    Uf= np.dot(d,Ff.T)
    uf_list=Uf.tolist()

    U=[0] * (len(ff)+len(cc))

    for x, y in zip(uf_list, ff):
        U[y]=x

    U=np.array(U)

    F= np.dot(glob_k,U)

    return F,U






