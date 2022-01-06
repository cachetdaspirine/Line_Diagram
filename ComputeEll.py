import numpy as np
from Get_High_L_Matrix import *
import tqdm
import sys

SimNum = int(sys.argv[1])

SeedBag = np.loadtxt('Seeds_With_Ell_Higher_5.dat',dtype=np.int64)
Ell0 = np.zeros(SeedBag.shape[0],dtype=float)
Nloop = SeedBag.shape[0]//10

for i in tqdm.trange(Nloop):
    Ell0[i+SimNum*Nloop] = MeasureLFromSeed(SeedBag[i+SimNum*Nloop])

np.save('Ell0'+str(SimNum),Ell0,allow_pickle=True)
