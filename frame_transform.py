import numpy as np
import math

def transform(x1, y1, x2, y2, k, pf):


    #calcluate the angle
    if x2 - x1 == 0:
        if y1 > y2:
            phi = -math.pi/2
        else:
            phi = math.pi/2
    else:
        phi=math.atan((y2-y1)/(x2-x1))

    #calcualte the cosine and sine of phi
    c = math.cos(phi)
    s = math.sin(phi)

    # build transformation factor
    t = np.array([[c,s,0,0,0,0],[-s,c,0,0,0,0],[0,0,1,0,0,0],[0,0,0,c,s,0],[0,0,0,-s,c,0],[0,0,0,0,0,1]])

    # transform stiffness
    k_trans = np.dot(t.T,np.dot(k,t))

    # transform fabricated forces
    Qf= np.dot(t.T, pf)

    return k_trans, Qf, t