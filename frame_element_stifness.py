#import needed libraries
import numpy as np
import math


from frame_data_input import *

def frame_element_stifness(x1,y1,x2,y2,E,A,I, P, M, W, Th, delta, mr):

    #calcualte length of member
    L = math.sqrt((x2-x1)**2+(y2-y1)**2)

    # build fabricated forces vector
    # concentrated load
    a = P[0]
    p = P[1]
    b = L-a
    Pf = np.array([[0] , [(p*(b**2)*(3*a+b))/L**3] , [p*(a*b**2)/L**2] , [0],[p*((a**2)*(3*b+a))/L**3] , [-(p*(b*a**2)/L**2)]])

    # moment
    a = M[0]
    m = M[1]
    b = L-a
    Pf += np.array([[0] , [6*m*a*b/L**3] , [m*b*(2*a-b)/L**2] , [0] , [-(6*m*a*b/L**3)] , [-(m*a*(2*b-1)/L**2)]])

    # distribiuted load
    a = W[0]
    d = W[1]
    q = W[2]
    b = L-a
    Pf = Pf + np.array([[0] , [(q*d/L**3)*(((2*a+L)*b**2)+(0.25*(a-b)*d**2))] , [(q*d/L**2)*(a*(b**2)+((a-2*b)*d**2)/12)] , [0],[(q*d/L**3)*(((2*b+L)*a**2)-(0.25*(a-b)*d**2))] , [-((q*d/L**2)*(b*(a**2)+((b-2*a)*d**2)/12))]])

    # thermal load
    alpha = Th[0]
    Tu = Th[1]
    Tl = Th[2]
    h = Th[3]
    Pf += np.array([[E*A*alpha*(Tl+Tu)*0.5] , [0] , [E*I*alpha*(Tl-Tu)/h] , [-E*A*alpha*(Tl+Tu)*0.5] , [0] , [-E*I*alpha*(Tl-Tu)/h]])

    # settlment data
    delta1 = delta[0]
    delta2 = delta[1]
    setl = delta2 - delta1
    Pf += np.array([[0] , [12*E*I*setl/L**3] , [6*E*I*setl/L**2] , [0] , [-12*E*I*setl/L**3] , [6*E*I*setl/L**2]])

    # check for any moment release
    if mr[0] == 1:
        # case 1: moment release at left end    
        pf = Pf.T
        lst = pf.tolist()
        Pf = lst[0]


        k = np.array([[ (A*L**2)/I , 0 , 0 , -(A*L**2)/I , 0 , 0 ] , [ 0 , 3 , 0 , 0 , -3 , 3*L] , [ 0 , 0 , 0 , 0 , 0 , 0] , [ -(A*L**2)/I , 0 , 0 , (A*L**2)/I , 0 , 0] , [ 0 , -3 , 0 , 0 , 3 , -3*L] , [ 0 , 3*L , 0 , 0 , -3*L , 3*L**2]]) * (E*I/L**3)
        Pfr = np.array([[Pf[0]] , [Pf[1]-(1.5/L)*Pf[2]] , [0] , [Pf[3]] , [Pf[4]+(1.5/L)*Pf[2]], [Pf[5]-0.5*Pf[2]]])
        Pf = Pfr

    elif mr[1] == 1 :
        # case 2: moment release at right hand
        pf = Pf.T
        lst = pf.tolist()
        Pf = lst[0]

        k = np.array([[ (A*L**2)/I , 0 , 0 , -(A*L**2)/I , 0 , 0 ] , [ 0 , 3 , 3*L , 0 , -3 , 0] , [ 0 , 3*L , 3*L**2 , 0 , -3*L , 0] , [ -(A*L**2)/I , 0 , 0 , (A*L**2)/I , 0 , 0] , [ 0 , -3 , -3*L , 0 , 3 , 0] , [ 0 , 0 , 0 , 0 , 0 , 0]]) * (E*I/L**3)
        Pfr = np.array([[Pf[0]] , [Pf[1]-(1.5/L)*Pf[5]] , [Pf[2]-0.5*Pf[5]] , [Pf[3]] , [Pf[4]+(1.5/L)*Pf[5]], [0]])
        Pf = Pfr

    elif mr[0] == 1 and mr[1] == 1:
        # case 3: moment release at both ends
        pf = Pf.T
        lst = pf.tolist()
        Pf = lst[0]

        k = np.array([[ 1 , 0 , 0 , -1 , 0 , 0 ] , [ 0 , 0 , 0 , 0 , 0 , 0] , [ 0 , 0 , 0 , 0 , 0 , 0] , [ -1 , 0 , 0 , 1 , 0 , 0] , [ 0 , 0 , 0 , 0 , 0 , 0] , [ 0 , 0 , 0 , 0 , 0 , 0]]) * (E*I/L**3)
        Pfr = np.array([[Pf[0]] , [Pf[1]-(1/L)*(Pf[2]+Pf[5])] , [0] , [Pf[3]] , [Pf[4]+(1/L)*(Pf[2]+Pf[5])], [0]]) 
        Pf = Pfr

    else:
        # build element stifness matrix
        k = np.array([[A/L,0,0,-A/L,0,0] , [0,(12*I)/(L**3),(6*I)/(L**2),0,-(12*I)/(L**3),(6*I)/(L**2)] , [0,(6*I)/(L**2),(4*I)/(L),0,-(6*I)/(L**2),(2*I)/(L)] , [-A/L,0,0,A/L,0,0] , [0,-(12*I)/(L**3),-(6*I)/(L**2),0,(12*I)/(L**3),-(6*I)/(L**2)] , [0,(6*I)/(L**2),(2*I)/(L),0,-(6*I)/(L**2),(4*I)/(L)]]) * E

    return k, Pf