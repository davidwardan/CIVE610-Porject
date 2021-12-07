#import needed libraries
import numpy as np
import math


#define function
def truss_element_stiffness_NL(x1_new,y1_new,x2_new,y2_new,x1,y1,x2,y2, E,A):

    # under elastic behavior
    #calcualte length of member
    L=math.sqrt((x2-x1)**2+(y2-y1)**2) 
    
    #calcualte new length of member
    Lbar=math.sqrt((x2_new-x1_new)**2+(y2_new-y1_new)**2)

    #calcualte the cosine and sine of phi
    c=float((x2_new-x1_new)/Lbar)
    s=float((y2_new-y1_new)/Lbar)
    #calcluate the angle
    '''
    if x2_new - x1_new == 0:
        if y1_new > y2_new:
            phi = -math.pi/2
        else:
            phi = math.pi/2
    else:
        phi=math.atan((y2_new-y1_new)/(x2_new-x1_new))
    '''

    #c=math.cos(phi)
    #s=math.sin(phi)

    #build stiffness matrix of the element
    Ke=np.array([[c**2,c*s,-c**2,-c*s],[c*s,s**2,-c*s,-s**2],[-c**2,-c*s,c**2,c*s],[-c*s,-s**2,c*s,s**2]])
    Ke=Ke*(E*A/(L))

    u = L - Lbar
    Q = ((E*A)/L)*u

    #build stiffness matrix of the element
    Kg=np.array([[-s**2,c*s,s**2,-c*s],[c*s,-c**2,-c*s,c**2],[s**2,-c*s,-s**2,c*s],[-c*s,c**2,c*s,-c**2]])
    Kg=Kg*(Q/Lbar)
    
    # calculate element stiffness matrix
    Kt = np.add(Ke,Kg)

    # build force vector
    Ft = np.array([[Q*c],[Q*s],[-Q*c],[-Q*s]])
    Ft = np.reshape(Ft, (4,1))
    return Kt ,Ft