# In this function :
# -> we draw a random matrix with high ell0
# -> compute the line of prefered aggregate
# -> output the line with the other informations
import numpy as np
import tqdm
from Get_Best_Aggregate import *
from Get_High_L_Matrix import *
import sys
#sys.path.append('/home/hcleroy/Extra_Module_py')
sys.path.append('/home/hleroy/Simulation/Extra_Module_py')
import RandomParticleFunctions_v4 as RPF
from Numeric_Hex_Energy import *


Nline = 50
Forbiden_seeds = set()
Lines = np.zeros(Nline,dtype=np.ndarray)
# we also stor GammaMaxS, not sure I ll use it though...
GammaMaxS = np.zeros(Nline,dtype=float)
#Seeds = np.zeros(Nline,dtype=np.int64)
#Ell0s = np.zeros(Nline,dtype=float)
Ell0s = np.load('Ell0.npy')

#parameter of get line diagram also usefull for the plot part
#Number of points in the line
NpointsGamma=100
#fibers max width
Wmax = 10
# hexagon max size
Nmax = 1000
SimNum = int(sys.argv[1])


#SeedBag = np.load('SeedBag400.npy')
SeedBag = np.loadtxt('Seeds_With_Ell_Higher_5.dat',dtype=np.int64)
Seeds = SeedBag[SimNum*Nline:(SimNum+1)*Nline]

for n in tqdm.trange(Nline):
    # Generate a matrix with ell0 high enough : ell0>ellmin
    #Seeds[n],Ell0s[n] = Get_High_L_Matrix(Forbiden_seeds=Forbiden_seeds,ellmin=3.5)
    #Forbiden_seeds.add(Seeds[n])
    Mc,rho0,eps1,eps2,seed = RPF.RandomParticle(Seeds[n])
    #Ell0s[n] = MeasureL(Mc,rho0)


    # Make the corresponding matrix
    Mc,rho0,e1,e2,Seeds[n] = RPF.RandomParticle(seed = Seeds[n])
    # generate the line, which has the size NpointsGamma
    Lines[n], GammaMaxS[n] = Make_Line_Diagram(Mc,rho0,e1,e2,NpointsGamma=NpointsGamma,Nmax=Nmax,Wmax=Wmax)



import Shape as Sh
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import cm
cmaplist = [(86./255,42./255.,132./255.,1.), (156./255,18/255.,109/255.,1.),(204./255.,35./255.,129./255.),(0,0,0,1)]
cmap = mcolors.LinearSegmentedColormap.from_list(
    'Custom cmap', cmaplist, 3)
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


WidthMax=Wmax
Nmax = Nmax

#Intricated way to compute size max
Size = int(1./6.* (3+np.sqrt(3*(4*Nmax-1))))
NList = np.array([Sh.Np(Sh.Parallel(r,'Hexagon')) for r in np.arange(1,Size+1,1)])
SizeMax=NList[-1]

np.save('Line'+str(SimNum),Lines,allow_pickle=True)
np.save('Gamma'+str(SimNum),GammaMaxS,allow_pickle=True)
np.save('Seed'+str(SimNum),Seeds,allow_pickle=True)
np.save('Ell0'+str(SimNum),Ell0s,allow_pickle=True)

GammaRange = np.linspace(0,1.,NpointsGamma)
fig,ax = plt.subplots(ncols=1,nrows=Nline,figsize=(15, Lines.shape[0]))
for n in range(Nline):
    #Define the masked array corresponding to the three regions
    HexRegion = np.ma.masked_array([Lines[n][:,1],Lines[n][:,1]],(np.array([Lines[n][:,1],Lines[n][:,1]])==0)| (np.array([Lines[n][:,1],Lines[n][:,1]])==SizeMax))
    FiberRegion = np.ma.masked_array([Lines[n][:,0],Lines[n][:,0]],np.array([Lines[n][:,0],Lines[n][:,0]])<=1)
    LacnarBulkRegion = np.ma.masked_array([Lines[n][:,2],Lines[n][:,2]],np.array([Lines[n][:,2],Lines[n][:,2]])==0)
    BulkRegion = np.ma.masked_array([Lines[n][:,1],Lines[n][:,1]],np.array([Lines[n][:,1],Lines[n][:,1]])!=SizeMax)

    # Nu defines the Y axis of each line
    NU = [-1,1]

    #Plot the different colors
    ax[Nline-n-1].pcolormesh([GammaRange,GammaRange],NU,HexRegion,cmap=cm.Reds,vmin=1,vmax=SizeMax,shading='auto')#,norm=mcolors.LogNorm()
    #ax[Nline-n-1].pcolormesh([GammaRange,GammaRange],NU,BulkRegion,cmap=cmap,shading='auto')
    ax[Nline-n-1].pcolormesh([GammaRange,GammaRange],NU,LacnarBulkRegion,cmap=cmap,shading='auto')
    ax[Nline-n-1].pcolormesh([GammaRange,GammaRange],NU,FiberRegion,cmap=cm.Blues,shading='auto')
    #ax[Nmax-n-1].set_yticklabels([truncate(Parameter[n,0],3)])
    #ax[Nmax-n-1].set_yticklabels([truncate(Pline[n],3)])
    if n!=0:
        ax[Nline-n-1].tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)
    #ax[Lines.shape[0]-n-1].pcolormesh([GammaRange,GammaRange],NU,Fiber2Region,cmap=cm.Greens,vmin=1,vmax=WidthMax)
ax[-1].set_xlabel(r'$\frac{\Gamma}{\Gamma_{max}}$',fontsize=30)
ax[ax.__len__()//2].set_ylabel(r'$\nu$',fontsize=30)
fig.savefig('RandomPhaseDiagram'+str(Number)+'.pdf',transparent=True,bbox_inches='tight')
#fig.savefig('RandomPhaseDiagram_3.png',transparent=True,bbox_inches='tight')
#plt.imshow([Lines[:,2][0],np.arange(0.,1.5,0.02)])
