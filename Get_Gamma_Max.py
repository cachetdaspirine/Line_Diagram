# This function returns the Gamma max associated to a specific matrix
import numpy as np
def Get_Gamma_Max(bf,bh,P,dGamma = 0.01):
    Neq=0
    if bh:
        while Neq < bh.Nmax:
            P.reComputeJ(P.Gamma+dGamma)
            Neq,E = bh.Get_Best_Disk(P)
        GammaHex = P.Gamma
    else:
        GammaHex=0.
    P.reComputeJ(0.)
    Weq=0
    while Weq < bf.Wmax-1:
        P.reComputeJ(P.Gamma+dGamma)
        Weq,E = bf.Get_Best_Fiber(P,type=1)
    return max(GammaHex,P.Gamma)
