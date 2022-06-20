# In this function :
# -> we draw a random matrix with high ell0
# -> compute the line of prefered aggregate
# -> output the line with the other informations
import numpy as np
from numpy.random import default_rng
#import tqdm
from Get_Best_Aggregate import *
from Get_High_L_Matrix import *
import sys
sys.path.append('/home/hcleroy/Extra_Module_py')
sys.path.append('/home/hleroy/Simulation/Extra_Module_py')
sys.path.append('/home/hcleroy/Extra_Module_py')
import RandomParticleFunctions_v4 as RPF
from Numeric_Hex_Energy import *



#parameter of get line diagram also usefull for the plot part
#Number of points in the line
OUTPUT = 'ALL'
NpointsGamma=100
#fibers max width
Wmax = 50
# hexagon max size
Nmax = 5000
SimNum = int(sys.argv[1])
SimMax = int(sys.argv[2])
Folder = sys.argv[3]+'/'
File = sys.argv[4]
NparticlesTotal = int(sys.argv[5])
Nline = NparticlesTotal//SimMax

Seeds = np.load(Folder+File+'SEED.npy')
Nus = np.load(Folder+File+'NU.npy')
Ell0s=np.load(Folder+File+'ELL.npy')

if Seeds.shape[0]!=NparticlesTotal:
    # if the number of particle asked time the number of Simulation
    # is not equal to the total seed size, then we randomly draw
    # the amount asked, homogeneously within the whole array.
    rng = default_rng()
    Nstep = Seeds.shape[0]//SimMax
    indexs = rng.choice(Nstep,size=Nline,replace=False)
    Seeds = Seeds[SimNum*Nstep:(SimNum+1)*Nstep][indexs]
    Nus = Nus[SimNum*Nstep:(SimNum+1)*Nstep][indexs]
    Ell0s=Ell0s[SimNum*Nstep:(SimNum+1)*Nstep][indexs]
    #print(Nus,SimNum,sep=' ')
    #sys.exit()
else:
    Seeds = Seeds[SimNum*Nline:(SimNum+1)*Nline]
    Nus = Nus[SimNum*Nline:(SimNum+1)*Nline]
    Ell0s=Ell0s[SimNum*Nline:(SimNum+1)*Nline]

# we also stor GammaMaxs
GammaMaxS = np.zeros(Seeds.shape[0],dtype=float)
Lines = np.zeros(Seeds.shape[0],dtype=np.ndarray)
if OUTPUT=='all' or OUTPUT == 'ALL':
    Energy = Lines = np.zeros(Seeds.shape[0],dtype=np.ndarray)


for n in range(Seeds.shape[0]):
    # Generate a matrix with ell0 high enough : ell0>ellmin
    #Seeds[n],Ell0s[n] = Get_High_L_Matrix(Forbiden_seeds=Forbiden_seeds,ellmin=3.5)
    #Forbiden_seeds.add(Seeds[n])
    #Mc,rho0,eps1,eps2,seed = RPF.RandomParticle(Seeds[n])
    #Ell0s[n] = MeasureL(Mc,rho0)


    # Make the corresponding matrix
    Mc,rho0,e1,e2,Seeds[n] = RPF.RandomParticle(seed = Seeds[n])
    # generate the line, which has the size NpointsGamma
    if OUTPUT == 'all' or OUTPUT=='ALL':
        Lines[n], GammaMaxS[n], Energy[n] = Make_Line_Diagram_ouput_all(Mc,rho0,e1,e2,NpointsGamma=NpointsGamma,Nmax=Nmax,Wmax=Wmax)
    else:
        Lines[n], GammaMaxS[n] = Make_Line_Diagram(Mc,rho0,e1,e2,NpointsGamma=NpointsGamma,Nmax=Nmax,Wmax=Wmax)



# import Shape as Sh
# import matplotlib.pyplot as plt
# import matplotlib.colors as mcolors
# from matplotlib import cm
# cmaplist = [(86./255,42./255.,132./255.,1.), (156./255,18/255.,109/255.,1.),(204./255.,35./255.,129./255.),(0,0,0,1)]
# cmap = mcolors.LinearSegmentedColormap.from_list(
#     'Custom cmap', cmaplist, 3)
# def truncate(number, digits) -> float:
#     stepper = 10.0 ** digits
#     return math.trunc(stepper * number) / stepper
#
#
# WidthMax=Wmax
# Nmax = Nmax

#Intricated way to compute size max
Size = int(1./6.* (3+np.sqrt(3*(4*Nmax-1))))
NList = np.array([Sh.Np(Sh.Parallel(r,'Hexagon')) for r in np.arange(1,Size+1,1)])
SizeMax=NList[-1]

print(SizeMax)

if OUTPUT=='all' or OUTPUT=='ALL':
    np.save(Folder+'Energy'+str(SimNum)+'.npy',Energy,allow_pickle=True)
np.save(Folder+'Line'+str(SimNum)+'.npy',Lines,allow_pickle=True)
np.save(Folder+'Gamma'+str(SimNum)+'.npy',GammaMaxS,allow_pickle=True)
np.save(Folder+'Seed'+str(SimNum)+'.npy',Seeds,allow_pickle=True)
np.save(Folder+'Ell0'+str(SimNum)+'.npy',Ell0s,allow_pickle=True)

# GammaRange = np.linspace(0,1.,NpointsGamma)
# fig,ax = plt.subplots(ncols=1,nrows=Nline,figsize=(15, Lines.shape[0]))
# for n in range(Nline):
#     #Define the masked array corresponding to the three regions
#     HexRegion = np.ma.masked_array([Lines[n][:,1],Lines[n][:,1]],(np.array([Lines[n][:,1],Lines[n][:,1]])==0)| (np.array([Lines[n][:,1],Lines[n][:,1]])==SizeMax))
#     FiberRegion = np.ma.masked_array([Lines[n][:,0],Lines[n][:,0]],np.array([Lines[n][:,0],Lines[n][:,0]])<=1)
#     LacnarBulkRegion = np.ma.masked_array([Lines[n][:,2],Lines[n][:,2]],np.array([Lines[n][:,2],Lines[n][:,2]])==0)
#     BulkRegion = np.ma.masked_array([Lines[n][:,1],Lines[n][:,1]],np.array([Lines[n][:,1],Lines[n][:,1]])!=SizeMax)
#
#     # Nu defines the Y axis of each line
#     NU = [-1,1]

    #Plot the different colors
#     ax[Nline-n-1].pcolormesh([GammaRange,GammaRange],NU,HexRegion,cmap=cm.Reds,vmin=1,vmax=SizeMax,shading='auto')#,norm=mcolors.LogNorm()
#     #ax[Nline-n-1].pcolormesh([GammaRange,GammaRange],NU,BulkRegion,cmap=cmap,shading='auto')
#     ax[Nline-n-1].pcolormesh([GammaRange,GammaRange],NU,LacnarBulkRegion,cmap=cmap,shading='auto')
#     ax[Nline-n-1].pcolormesh([GammaRange,GammaRange],NU,FiberRegion,cmap=cm.Blues,shading='auto')
#     #ax[Nmax-n-1].set_yticklabels([truncate(Parameter[n,0],3)])
#     #ax[Nmax-n-1].set_yticklabels([truncate(Pline[n],3)])
#     if n!=0:
#         ax[Nline-n-1].tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)
#     #ax[Lines.shape[0]-n-1].pcolormesh([GammaRange,GammaRange],NU,Fiber2Region,cmap=cm.Greens,vmin=1,vmax=WidthMax)
# ax[-1].set_xlabel(r'$\frac{\Gamma}{\Gamma_{max}}$',fontsize=30)
# ax[ax.__len__()//2].set_ylabel(r'$\nu$',fontsize=30)
# fig.savefig('RandomPhaseDiagram'+str(SimNum)+'.pdf',transparent=True,bbox_inches='tight')
#fig.savefig('RandomPhaseDiagram_3.png',transparent=True,bbox_inches='tight')
#plt.imshow([Lines[:,2][0],np.arange(0.,1.5,0.02)])
