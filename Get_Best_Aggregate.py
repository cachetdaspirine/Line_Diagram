# This function returns the best aggregate as an array for
# a given Gamma
import numpy as np
import sys
from Get_Gamma_Max import *
sys.path.append('/home/hcleroy/Extra_Module_py')
sys.path.append('/home/hleroy/Simulation/Extra_Module_py')
sys.path.append('/home/hcleroy/Extra_Module_py')
import Conversion as Conv
from Numeric_Fiber_Energy import *
from Numeric_Hex_Energy import *

def Make_Line_Diagram(Mc,rho0,e1,e2,NpointsGamma = 100,Nmax = 1000,Wmax=10):
    # Line contain the result : it's a row of NpointsGamma
    # Each entry of this row tells which aggregate is best:
    # [w (fiber), S (Disk), 1 (Lacunar BUlk)]
    Line = np.zeros((NpointsGamma,3),dtype=int)
    # Build the get best fiber/disk objects
    Param = Conv.MatrixToContinuum(Mc,rho0,e1,e2,Gamma=0.)
    bh = BD(Nmax,Param,Expansion=True,Mc=Mc,q0=rho0)
    bf = BF(Wmax,Param,Expansion=True,Mc=Mc,q0=rho0)
    # Compute GammaMax, which implies to already Compute
    # the energy of the big aggregates
    GammaMax = Get_Gamma_Max(bf,bh,Param,dGamma = 1/NpointsGamma)
    #loop over gamma
    for n,gamma in enumerate(np.linspace(0.,GammaMax,NpointsGamma)):
        #adjust gamma in a conversion object
        Param = Conv.MatrixToContinuum(Mc,rho0,e1,e2,Gamma=gamma)
        #compute the best disk and fiber
        BestDisk = bh.Get_Best_Disk(Param)
        BestFiber = bf.Get_Best_Fiber(Param,type=1)
        ELacunar = 3*Param.J
        # Compare the energy of each of them, and fill the entry of
        # Line accordingly
        if BestDisk[1]>=ELacunar and BestFiber[1]>=ELacunar:
            Line[n] = np.array([0,0,1])
        elif BestDisk[1]>BestFiber[1]:
            Line[n] = np.array([BestFiber[0],0,0])
        else:
            Line[n] = np.array([0,BestDisk[0],0])
    return Line,GammaMax
