import numpy as np
from Get_High_L_Matrix import *
import os

nparticles = 10
ellmin = 5
if not os.path.isfile('touch Seeds_With_Ell_Higher_'+str(ellmin)+'.dat'):
    os.system('touch Seeds_With_Ell_Higher_'+str(ellmin)+'.dat')
file = open('Seeds_With_Ell_Higher_'+str(ellmin)+'.dat','ab')

for i in range(nparticles):
    #SeedsFile = open('Seeds_With_Ell_Higher_'+str(ellmin)+'.dat','r')
    #Forbiden_seeds = {np.int64(f) for f in np.array(SeedsFile.read().split("\n"))[:-1]}
    Forbiden_seeds = set(np.loadtxt('Seeds_With_Ell_Higher_'+str(ellmin)+'.dat',dtype=np.int64))
    seed,ell0 = Get_High_L_Matrix(Forbiden_seeds = Forbiden_seeds,ellmin=ellmin)

    np.savetxt(file,np.int64(np.array([seed])),fmt='%i')
file.close()
