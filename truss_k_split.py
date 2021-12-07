import numpy as np
from truss_data_input import *

def split_matrix(glob_K, MSUP):


    # sort joints into free and constraint
    joint_C = MSUP[:,0]
    joint = list(range(1,NJ))
    joint_F=list(set(joint) - set(joint_C))
    
    
    '''
    ff=[]
    for i in joint_F:
        ff.append((2*i)-2)
        ff.append(2*i-1)
    cc=[]
    for i in joint_C:
        cc.append((2*i)-2)
        cc.append(2*i-1)
    '''
    # get DOF for free and constraint
    ff=[]
    cc=[]
    i=0
    for row in MSUP:
        n=2*i
        if row[0] == 0:
            ff.append(n)
        elif row[0] ==1:
            cc.append(n)

        if row[1] == 0:
            ff.append(n+1)
        elif row[1] == 1:
            cc.append(n+1)
        i+=1


    # iterate over the free dofs and build kff
    kff = np.zeros((len(ff),len(ff)))

    r=0
    
    for i in ff:
        c=0
        for j in ff:
            #print(r,c,i,j)
            kff[r][c] += glob_K[i][j]
            c+=1
        r+=1



    # iterate over the constraint dofs and build kcc
    kcc = np.zeros((len(cc),len(cc)))

    r=0
    for i in cc:
        c=0
        for j in cc:
            kcc[r][c] += glob_K[i][j]
            c+=1
        r+=1

    

    # build kfc and kcf

    kfc= np.zeros((len(ff),len(cc)))
    r=0
    for i in ff:
        c=0
        for j in cc:
            kfc[r][c] += glob_K[i][j]
            c+=1
        r+=1


    kcf= np.zeros((len(cc),len(ff)))
    r=0
    for i in cc:
        c=0
        for j in ff:
            kcf[r][c] += glob_K[i][j]
            c+=1
        r+=1        

    return kff, kcc, kfc, kcf, ff, cc