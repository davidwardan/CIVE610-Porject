# import needed libraries
import numpy as np
import matplotlib.pyplot as plt
import math


# get input data
from truss_data_input import * # this will load all variables from data_input file

# get global stiffness matrix of truss structure
from truss_global_stiffness import truss_global_stiffness
glob_k_e = truss_global_stiffness(COORD, MPRP, EM, CP) # elastic behavior

# this functions splits global stiffness matrix
from truss_k_split import split_matrix
kff_e, kcc_e, kfc_e, kcf_e, ff, cc = split_matrix(glob_k_e, MSUP)

# get force and displacement vectors
from truss_f_d import truss_f_d
F, Uprev = truss_f_d(glob_k_e, kff_e, kcf_e, MSUP, PJ, ff, cc)

tolerance = 1

while tolerance >= 0.01:

    # get new deformed coordinates of truss
    from truss_deformed import deformed_COORD
    COORD_new = deformed_COORD(COORD, Uprev)

    # start ietartions here ...

    # get global parameters
    from truss_global_stiffness_NL import truss_global_stiffness_NL
    glob_k, glob_f = truss_global_stiffness_NL(COORD_new, COORD, MPRP, EM, CP)

    # split matrix 
    from truss_k_split import split_matrix
    kff, kcc, kfc, kcf, ff, cc = split_matrix(glob_k, MSUP)

    # split force vector
    f_ff = glob_f[ff]

    # split applied force vector
    fr = []
    for row in PJ:
        for i in row:
            fr.append(i)

    fr = np.transpose(np.array([fr]))
    fr_ff = fr[ff]

    # subtract forces

    f = np.subtract(fr_ff,f_ff)

    delta_d = np.dot(np.linalg.inv(kff), f)

    u = Uprev[ff]
    u = np.transpose(u)
    u = np.reshape(u, (len(ff),1))

    tolerance = math.sqrt( np.sum(delta_d*delta_d)/np.sum(u*u))

    u_ = np.add(delta_d,u)

    uf_list = u_.tolist()

    U=[0] * (len(ff)+len(cc))

    for x, y in zip(uf_list, ff):
        U[y]=x[0]

    Uprev=np.array(U)








