# import needed libraries
import numpy as np
import matplotlib.pyplot as plt

'''
the following function is used to exucute all other functions
this file is specific for truss analysis
'''

# get input data
from truss_data_input import * # this will load all variables from data_input file

# get global stiffness matrix of truss structure
from truss_global_stiffness import truss_global_stiffness
glob_k = truss_global_stiffness(COORD, MPRP, EM, CP)

# this functions splits global stiffness matrix
from truss_k_split import split_matrix
kff, kcc, kfc, kcf, ff, cc = split_matrix(glob_k, MSUP)

# get force and displacement vectors
from truss_f_d import truss_f_d
F, U = truss_f_d(glob_k, kff, kcf, MSUP, PJ, ff, cc)

# get deformed coordinates of truss
from truss_deformed import deformed_COORD
COORD_new = deformed_COORD(COORD, U)

# get coordinates for truss system
from plot_COORD import  get_plot_COORD
COORD_plot = get_plot_COORD(COORD, MPRP)
x = COORD_plot[:,0] # collect x coordinates
y = COORD_plot[:,1] # collect y coordinates


# get coordinates for truss deformed shape
COORD_new_plot = get_plot_COORD(COORD_new, MPRP)
x_new = COORD_new_plot[:,0] 
y_new = COORD_new_plot[:,1]


# Plotting both the curves simultaneously
plt.plot(x, y, color='r', label='original')
plt.plot(x_new, y_new, color='g', label='deformed')

plt.legend()
plt.show()