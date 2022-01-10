import numpy as np
from Get_High_L_Matrix import *
import os

nparticles = 20
ellmin = 5
#if not os.path.isfile('touch Seeds_With_Ell_Higher_'+str(ellmin)+'_bis.dat'):
#    os.system('touch Seeds_With_Ell_Higher_'+str(ellmin)+'_bis.dat')
file = open('Seeds_With_Ell_Higher_'+str(ellmin)+'_bis.dat','a')

for i in range(nparticles):
    #SeedsFile = open('Seeds_With_Ell_Higher_'+str(ellmin)+'.dat','r')
    #Forbiden_seeds = {np.int64(f) for f in np.array(SeedsFile.read().split("\n"))[:-1]}
    try:
        Forbiden_seeds = set(np.loadtxt('Seeds_With_Ell_Higher_'+str(ellmin)+'_bis.dat',dtype=np.int64))
    except TpeError:
        try:
            Forbiden_seeds = set([float(np.loadtxt('Seeds_With_Ell_Higher_'+str(ellmin)+'_bis.dat',dtype=np.int64))])
        except:
            raise
    seed,ell0 = Get_High_L_Matrix(Forbiden_seeds = Forbiden_seeds,ellmin=ellmin)

    #np.savetxt(file,np.array([seed],dtype=np.int64))
    file.write(str(seed)+'\n')
file.close()
