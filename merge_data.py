import numpy as np
import sys

SimMax = sys.argv[1]
dir_name = sys.argv[2]

seed = np.load(dir_name+'Seed0.npy')
Gamma = np.load(dir_name+'Gamma0.npy')
Line = np.load(dir_name+'Line0.npy',allow_pickle=True)
Ell0 = np.load(dir_name+'Ell0.npy')
for i in range(1,SimMax):
    seed = np.append(seed,np.load(dir_name+'Seed'+str(i)+'.npy'))
    Gamma = np.append(Gamma,np.load(dir_name+'Gamma'+str(i)+'.npy'))
    Line = np.append(Line,np.load(dir_name+'Line'+str(i)+'.npy'),axis=0)
    Ell0 = np.append(Ell0,np.load(dir_name+'Ell'+str(i)+'.npy'))

np.save(dir_name+'final_seed.npy',seed)
np.save(dir_name+'final_GammaMax.npy',Gamma)
np.save(dir_name+'final_Line.npy',Line,allow_pickle=True)
np.save(dir_name+'final_ell.npy',Ell0)
