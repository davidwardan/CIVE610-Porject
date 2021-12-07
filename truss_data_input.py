import numpy as np


'''
data_ input serves to collect data from the user regarding the structure of interest
this includes joint data, support data, material property, section properties, member data, and load data
'''

# Joint Data
COORD = np.array([[0,0],[192,0],[96,72],[96,144]]) # create coordinate matrix
NJ=np.size(COORD, 0)

# Support Data
MSUP = np.array([[1,1],[1,1],[0,0],[1,1]]) # support data matrix MSUP in order of joints

# Material Property (E)
EM = np.array([[1300],[1300],[1300]]) # insert in order of members

# Cross-Sectional Property
CP= np.array([[2],[2],[1]]) # insert in order of members

# Member Data
MPRP=np.array([[1,3],[2,3],[3,4]]) # starting joint, end joint # in order of memebers

# Load Data
PJ=np.array([[0,0],[0,0],[400,-800],[0,0]]) # insert in order of joints

