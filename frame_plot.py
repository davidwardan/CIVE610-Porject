import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

def plot_MDR(R1, M1, v1 ,r1,R2, M2, v2 ,r2, L, a, P , b ,Mnt, w ,E ,I):

    
    '''
    # define inputs
    # reactions at joints
    R1= 13.5
    M1 = 0
    R2 = 6.5
    M2 = 0

    # displacements at joints
    v1 = 0
    r1 = 0
    v2 = 0
    r2 =  0 

    # define time step for plotting
    dx=0.1
    L = 10000
    t = [i for i in np.arange(0,L,dx)]


    # define moment equation for point load
    # point load data
    a = 5000
    P = 20

    # concentrated moment load data
    b = 2000
    Mnt = 35000

    # distributed load data
    w = 0.001
    '''
    # define time step for plotting
    dx=0.1
    t = [i for i in np.arange(0,L,dx)]

    # intitiate lists
    S =[]
    M=[]
    v=[]
    r=[]

    # case 1: only distributed
    if Mnt == 0 and P==0 and w != 0:
        for x in t:
                S.append(-w*x + R1)
                M.append(-M1 + R1*x -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  -w*(1/6)*x**3)*(1/(E*I))+ r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  -w*(1/24)*x**4)*(1/(E*I)) +r1*x + v1)


    # case 2: only concetrated point load
    elif Mnt == 0 and P!=0 and w == 0:
        for x in t:
            if x >= 0 and x < a :
                S.append(-w*x + R1)
                M.append(-M1 + R1*x -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  -w*(1/6)*x**3)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  -w*(1/24)*x**4)*(1/(E*I)) +r1*x+ v1)
            else: # needs fixing
                S.append(-w*x + R1 - P)
                M.append(-M1 + R1*x - P*(x-a) - Mnt -w*0.5*x**2)
                c1 = (M1*L - R1*0.5*L**2  + P*(0.5*(L**2) - a*L))*(1/(E*I)) + r2
                r.append((-M1*x + R1*0.5*x**2  - P*(0.5*(x**2) - a*x))*(1/(E*I)) + c1)
                c2 = (M1*0.5*L**2 - R1*(1/6)*L**3  + P*((1/6)*(L**3) - a*0.5*L**2))*(1/(E*I)) -c1*L + v2
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  - P*((1/6)*(x**3) - a*0.5*x**2))*(1/(E*I)) +c1*x + c2)


    # case 3: only concentrated moment
    elif  Mnt != 0 and P==0 and w == 0:
        for x in t:
            if x >= 0 and x < b :
                S.append(-w*x + R1)
                M.append(-M1 + R1*x)
                r.append((-M1*x + R1*0.5*x**2)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3)*(1/(E*I)) +r1*x + v1)
            else: # needs fixing
                S.append(-w*x + R1)
                M.append(-M1 + R1*x  - Mnt)
                c1 = (M1*L - R1*0.5*L**2  + Mnt*L)*(1/(E*I)) + r2
                r.append((-M1*x + R1*0.5*x**2  - Mnt*x )*(1/(E*I)) + c1)
                c2 = (M1*0.5*L**2 - R1*(1/6)*L**3  + Mnt*0.5*L**2)*(1/(E*I)) -c1*L + v2
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  - Mnt*0.5*x**2)*(1/(E*I)) +c1*x+ c2) 

    # case 4: no loads
    else:
        for x in t:
            S.append(R1)
            M.append(-M1 + R1*x )
            r.append((-M1*x + R1*0.5*x**2)*(1/(E*I))+ r1)
            v.append((-M1*0.5*x**2 + R1*(1/6)*x**3)*(1/(E*I)) +r1*x + v1)  


    '''   
   # case 1: only distributed
    if b > a:
        for x in t:
            if x >= 0 and x < a :
                S.append(-w*x + R1)
                M.append(-M1 + R1*x -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  -w*(1/6)*x**3)*(1/(E*I))+ r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  -w*(1/24)*x**4)*(1/(E*I)) +r1*x + v1)
            elif x >= a and x < b :
                S.append(-w*x + R1 - P)
                M.append(-M1 + R1*x - P*(x-a) -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  - P*(0.5*(x**2) - a*x) -w*(1/6)*x**3)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  - P*((1/6)*(x**3) - a*0.5*x**2) -w*(1/24)*x**4)*(1/(E*I)) +r1*x + v1)
            else:
                S.append(-w*x + R1 - P)
                M.append(-M1 + R1*x - P*(x-a) - Mnt -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  - P*(0.5*(x**2) - a*x) - Mnt*x -w*(1/6)*x**3)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  - P*((1/6)*(x**3) - a*0.5*x**2) - Mnt*0.5*x**2 -w*(1/24)*x**4)*(1/(E*I))   +r1*x + v1)


    # case 2: only concetrated
    elif a > b:
        for x in t:
            if x >= 0 and x < b :
                S.append(-w*x + R1)
                M.append(-M1 + R1*x -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  -w*(1/6)*x**3)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  -w*(1/24)*x**4)*(1/(E*I)) +r1*x+ v1)
            elif x >= b and x < a :
                S.append(-w*x + R1)
                M.append(-M1 + R1*x - Mnt -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  - Mnt*x -w*(1/6)*x**3)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  - Mnt*0.5*x**2 -w*(1/24)*x**4)*(1/(E*I)) +r1*x + v1)
            else:
                S.append(-w*x + R1 - P)
                M.append(-M1 + R1*x - P*(x-a) - Mnt -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  - P*(0.5*(x**2) - a*x) - Mnt*x -w*(1/6)*x**3)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  - P*((1/6)*(x**3) - a*0.5*x**2) - Mnt*0.5*x**2 -w*(1/24)*x**4)*(1/(E*I)) +r1*x + v1)


    # case 3: only concentrated moment
    else:
        for x in t:
            if x >= 0 and x < a :
                S.append(-w*x + R1)
                M.append(-M1 + R1*x -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  -w*(1/6)*x**3)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  -w*(1/24)*x**4)*(1/(E*I)) +r1*x + v1)
            else:
                S.append(-w*x + R1 - P)
                M.append(-M1 + R1*x - P*(x-a) - Mnt -w*0.5*x**2)
                r.append((-M1*x + R1*0.5*x**2  - P*(0.5*(x**2) - a*x) - Mnt*x -w*(1/6)*x**3)*(1/(E*I)) + r1)
                v.append((-M1*0.5*x**2 + R1*(1/6)*x**3  - P*((1/6)*(x**3) - a*0.5*x**2) - Mnt*0.5*x**2 -w*(1/24)*x**4)*(1/(E*I)) +r1*x+ v1) 
        ''' 

    fig, ax = plt.subplots(4,1)
    fig.set_size_inches(18.5, 10.5)

    ax[0].plot(t, S , color ='purple')
    ax[0].set_title('Shear Diagram')

    ax[1].plot(t, M, color = "blue")
    ax[1].set_title('Moment Diagram')

    ax[2].plot(t, r ,color = "green")
    ax[2].set_title('Slope Diagram')

    ax[3].plot(t, v ,color = "red")
    ax[3].set_title('Deflection Diagram')



