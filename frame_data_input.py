import numpy as np


# Joint Data
COORD = np.array([[0,0],[8000,0],[13000,0]]) # create coordinate matrix
NJ=np.size(COORD, 0)

# Support Data
MSUP = np.array([[0,1,0],[0,1,0],[1,1,1]]) # Rx,Ry,Mz

# Material Property (E)
EM = np.array([[200],[200]]) # insert in order of members

# Cross-Sectional Property
CP= np.array([[6000],[4000]]) # insert in order of members

# Inertia Property
IP= np.array([[200000000],[50000000]]) # insert in order of members

# Member Data
MPRP=np.array([[1,2],[2,3]]) # starting joint, end joint # in order of memebers

# Moment releases
MR = np.array([[0,0],[0,0]]) # each row represents a member with each column represetning a node with value "1" for releases

# Load Data
# this apllication will take into consideration three type of loads P, M, and W
P=np.array([[0, 0],[2000,20]]) # (a, p) and order is in order of members
M=np.array([[4000, 3500],[0,0]]) # (a, M) and order is in order of members
W=np.array([[0, 0, 0],[0,0,0]]) # (a, d, W) and order is in order of members
Th=np.array([[0,0,0,400],[0,0,0,400]]) # aplha factor, Tupper, Tlower, h 
                                       # h cannot be 0 always assume a randome value if not given

# Load settlement data
Delta = np.array([[0,0],[0,0,0]]) # make sure that settlement is defined consistently thoughout the member

# Load joint external loads
PJ = np.array([[0,0,0],[0,0,0],[0,0,0]]) # Fx, Fy, Mz
