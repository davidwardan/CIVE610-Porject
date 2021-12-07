import numpy as np

def split_fabricated(ff ,cc, Ff):
    ''''
    # convert to numpy vector
    cons = np.array([cc])
    cons = np.transpose(cons)
    free = np.array([ff])
    free = np.transpose(free)

    # built transformation vector
    Tf = [0] * (len(ff)+len(cc))
    Tc = [0] * (len(ff)+len(cc))

    for i in cc:
        Tc[i] = 1

    for i in ff:
        Tf[i] = 1

    # get fabricated for free dof and for constrainted dof
    Tf = np.array([Tf])
    Tf = np.transpose(Tf)
    Ff_f = Ff * Tf

    Tc = np.array([Tc])
    Tc = np.transpose(Tc)
    Ff_c = Ff * Tc
    '''
    Ff_f = Ff[ff]
    Ff_c = Ff[cc]

    return Ff_c, Ff_f
    


