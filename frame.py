# import needed libraries
'''
the following function is used to exucute all other functions
this file is specific for frame analysis
'''

# get input data
from frame_data_input import * # this will load all variables from data_input file

# get global stiffness matrix of truss structure
from frame_global_stiffness import frame_global_stiffness
glob_K, Ff = frame_global_stiffness(COORD, MPRP, EM, CP, IP, P, M ,W , Th, Delta, MR)

#  this functions splits global stiffness matrix
from frame_k_split import split_matrix
kff, kcc, kfc, kcf, ff, cc = split_matrix(glob_K, MSUP)

# this functions splits the fabriacted forces
from frame_fabricated_split import split_fabricated
Ff_c, Ff_f = split_fabricated(ff ,cc, Ff)

# get displacement and forces vectors
from frame_f_d import frame_f_d
F, U = frame_f_d(kff, glob_K, Ff_f, PJ, ff, cc , Ff)

# plot moment displacement and slope diagrams
from frame_element_diagram import frame_elemt_diagram
frame_elemt_diagram(COORD, MPRP, EM, CP, IP, P, M ,W , F, U, Th, Delta, MR)