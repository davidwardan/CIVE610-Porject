import numpy as np

def frame_f_d(Kff, glob_k, Ff_f, PJ, ff, cc, Ff):

    # get external forces vector
    F = []

    for row in PJ:
        F.append(row[0])
        F.append(row[1])
        F.append(row[2])

    F = np.array(F)

    F_free = F[ff]
    F_free = np.transpose(F_free)
    F_free = np.reshape(F_free, (len(ff),1))




    # get displacements at free dofs
    uf = np.dot( np.linalg.inv(Kff) ,  np.add(F_free, Ff_f*-1))

    # get diplacment vector
    uf_list = uf.tolist()
    U = [0] * (len(ff)+len(cc))

    for x, y in zip(uf_list, ff):
        U[y] = x[0]

    U = np.array(U)

    # get joint forces vector
    F = np.dot(glob_k,U) + Ff.T

    U = np.reshape(U, ((len(cc)+len(ff)), 1))
    F = F.T

    return F, U


