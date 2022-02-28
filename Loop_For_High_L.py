import numpy as np
from Get_High_L_Matrix import *
import copy
import os
import sys
#import tqdm

sim_num = int(sys.argv[1])
sim_max = int(sys.argv[2])
# name of the directory
dir_name = sys.argv[3]
seed = int(sys.argv[4])

nparticles = 10000
#ellmin = 0
#ellmax = 3

#last_seed = np.load('last_max_seed.npy')[0]
#np.save('last_max_seed.npy',[last_seed * nparticles])
#file = open('last_max_seed.txt','r')
#last_seed = int(file.read())
#file.close()
#file = open('last_max_seed.txt','w')
#file.write(str(last_seed+nparticles))
#file.close()
#np.savetxt('last_max_seed.txt',last_seed+nparticles)
#seed = last_seed + nparticles
Ell0s = np.zeros(nparticles,dtype=float)
Seeds = np.zeros(nparticles,dtype=np.int64)
for i in range(nparticles):
    #try:
    #    seeds_of_this_simulation = np.load(dir_name+'/Seeds_With_Ell_Higher_'+str(ellmin)+'_Smaller_'+str(ellmax)+'_'+str(sim_num)+'.npy')
    #except FileNotFoundError:
    #    seeds_of_this_simulation = np.array([],dtype=np.int64)
    seed += 1
    #forbiden_seeds = copy.copy(seeds_of_this_simulation)
    #for i in range(sim_max+1):
    #    try:
    #        forbiden_seeds = np.append(forbiden_seeds,np.load(dir_name+'/Seeds_With_Ell_Higher_'+str(ellmin)+'_Smaller_'+str(ellmax)+'_'+str(i)+'.npy'))
    #    except FileNotFoundError:
    #        pass
    #forbiden_seeds=set(forbiden_seeds)

    #seed,ell0 = Get_High_L_Matrix(seed)#ellmin=ellmin,ellmax=ellmax)

    Mc,rho0,eps1,eps2,seed = RPF.RandomParticle(seed=seed)#,distribution='exp')
    Ell0s[i] = MeasureL(Mc,rho0,shape='strips')
    Seeds[i] = seed
    #seeds_of_this_simulation = np.append(seeds_of_this_simulation,seed)
    #np.save(dir_name+'/Seeds_With_Ell_Higher_'+str(ellmin)+'_Smaller_'+str(ellmax)+'_'+str(sim_num)+'.npy',seeds_of_this_simulation)
np.save(dir_name+'/seed_'+str(sim_num)+'.npy',Seeds)
np.save(dir_name+'/Ell0s'+str(sim_num)+'.npy',Ell0s)
