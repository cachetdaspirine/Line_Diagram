# This function provide a matrix with a large characteristic length
# making sure that it is not already part of a given list of matrix
import numpy as np
import sys
import copy
import os
import matplotlib.pyplot as plt
sys.path.append('/home/hcleroy/Extra_Module_py')
sys.path.append('/home/hleroy/Simulation/Extra_Module_py')
import RandomParticleFunctions_v4 as RPF
import MeasurePoisson as MP
import Shape as Sh
import RandSyst as RSys

Name = str(np.random.randint(1000000))

def Get_High_L_Matrix(Forbiden_seeds = set(),ellmin = 2,ellmax=np.inf,count = False):
    keep = True
    counter = 0
    while keep:
        Mc,rho0,eps1,eps2,seed = RPF.RandomParticle()
        if not seed in Forbiden_seeds:
            ell0 = MeasureL(Mc,rho0)
            if ell0 > ellmin and ell0<ellmax:
                keep = False
            counter +=1
    if count:
        print(counter)
    return seed, ell0


def DistanceFromEdge(Array):
    Res = dict()
    box = copy.copy(Array)
    A,B = np.where(Array==1)
    Index = set(list(zip(A,B)))
    ind = 0
    while Index.__len__()!=0:
        toremove=set()
        for ij in Index:
            if Sh.Get_Neighbors(box,ij,Free=True,ParticleType='Hexagon').__len__()!=0 or Sh.Get_Neighbors(box,ij,Border=True,ParticleType='Hexagon').__len__()!=0:
                Res[ij] = ind
                toremove.add(ij)
        #print(toremove)
        #input()
        for ij in toremove:
            box[ij]=0
        Index-=toremove
        ind+=1
    return Res
def MeasureLFromSeed(seed):
    Mc,rho0,eps1,eps2,seed = RPF.RandomParticle(seed=seed)
    return MeasureL(Mc,rho0)
def MeasureL(Mc,rho0,shape='hexagon'):
    if shape=='hexagon':
        return MeasureLHex(Mc,rho0)
    elif shape=='fiber':
        return MeasureLFiber(Mc,rho0)
    else:
        print('shape argument have to be either hexagon or fiber')
        raise AttributeError
def MeasureLFiber(Mc,rho0,width=10):
    Sys = RSys.System(Mc,rho0,Sh.Fiber(5*width,width,'Hexagon'))
    EnergyData = Sys.get_sites_energy_as_array()
    E = np.array([np.mean(EnergyData[10:-10,depth]) for depth in range(width//2-1)])
    return E
def MeasureLHex(Mc,rho0,check=False):
    Array = Sh.Parallel(18,ParticleType='Hexagon')
    #Array = Sh.Fiber(10,50,ParticleType='Hexagon')
    S = RSys.System(Mc,rho0,Array)
    S.PrintPerSite(Name = Name,Extended=True)
    EnergyData = np.loadtxt(Name)
    os.system('rm '+Name)
    Ranking = DistanceFromEdge(Array)
    Res = np.zeros((max(Ranking.values())+1,2),dtype=float)
    for ligne in EnergyData:
        Res[Ranking[(int(ligne[-2]),int(ligne[-1]))],0] += ligne[-3]
        Res[Ranking[(int(ligne[-2]),int(ligne[-1]))],1] += 1
    #Res = Res[1:]
    Res[:,0] = Res[:,0]/Res[:,1]
    if check:
        plt.plot(np.arange(0,Res.shape[0],1),Res[:,0])
    return sum((max(Res[:,0])-Res[:,0])/(max(Res[:,0])-min(Res[:,0])))
