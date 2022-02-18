import numpy as np
from Get_High_L_Matrix import *
import copy
import os
import sys
import tqdm

sim_num = int(sys.argv[1])
sim_max = int(sys.argv[2])
# name of the directory
dir_name = sys.argv[3]

nparticles = 100
ellmin = 0
ellmax = 3

for i in tqdm.trange(nparticles):

    try:
        seeds_of_this_simulation = np.load(dir_name+'/Seeds_With_Ell_Higher_'+str(ellmin)+'_Smaller_'+str(ellmax)'_'+str(sim_num)+'.npy')
    except FileNotFoundError:
        seeds_of_this_simulation = np.array([],dtype=np.int64)
    forbiden_seeds = copy.copy(seeds_of_this_simulation)
    for i in range(sim_max+1):
        try:
            forbiden_seeds = np.append(forbiden_seeds,np.load(dir_name+'/Seeds_With_Ell_Higher_'+str(ellmin)+'_'+str(i)+'.npy'))
        except FileNotFoundError:
            pass
    forbiden_seeds=set(forbiden_seeds)

    seed,ell0 = Get_High_L_Matrix(Forbiden_seeds = forbiden_seeds,ellmin=ellmin,ellmax=ellmax)
    seeds_of_this_simulation = np.append(seeds_of_this_simulation,seed)
    np.save(dir_name+'/Seeds_With_Ell_Higher_'+str(ellmin)+'_'+str(sim_num)+'.npy',seeds_of_this_simulation)
