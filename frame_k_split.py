import numpy as np

def split_matrix(glob_K, MSUP):

    # get list of dof with value of 1 if constraint and 0 if free
    dof=[]
    for row in MSUP:
        for i in row:
            dof.append(i)

    # create list of degrees of freedom
    lst = list(range(1,len(dof)+1))

    # get cc and ff
    products = []
    for num1, num2 in zip(lst, dof):
	    products.append(num1 * num2)

    #products += -1
 
    cc = []
    ff = []

    for i in products:
        if i != 0:
            cc.append(i)

    for i in range(len(cc)):
        cc[i] = cc[i] -1

    lst = list(range(0,len(dof)))

    difference_1 = set(lst).difference(set(cc))
    difference_2 = set(cc).difference(set(lst))

    ff = list(difference_1.union(difference_2))

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









