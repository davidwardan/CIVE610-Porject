#import needed libraries
import numpy as np
import math
from numpy.core.fromnumeric import around


#define function
def truss_element_stiffness(x1,y1,x2,y2,E,A):

    #calcualte length of member
    L=math.sqrt((x2-x1)**2+(y2-y1)**2) 

    #calcluate the angle
    if x2 - x1 == 0:
        if y1 > y2:
            phi = -math.pi/2
        else:
            phi = math.pi/2
    else:
        phi=math.atan((y2-y1)/(x2-x1))

    #calcualte the cosine and sine of phi
    c=math.cos(phi)
    s=math.sin(phi)

    #build stiffness matrix of the element
    K=np.array([[c**2,c*s,-c**2,-c*s],[c*s,s**2,-c*s,-s**2],[-c**2,-c*s,c**2,c*s],[-c*s,-s**2,c*s,s**2]])
    K=K*(E*A/(L))

    np.around(K,decimals=1)

    return K