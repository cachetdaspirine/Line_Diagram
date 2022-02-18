import numpy as np
import copy

Folder = 'ellmin5_Wmax10_Nmax100_dGamma100_first_batch/'
Ell0s = np.load(Folder+'Ell00.npy',allow_pickle=True)
Gammas = np.load(Folder+'Gamma0.npy',allow_pickle=True)
Lines = np.load(Folder+'Line0.npy',allow_pickle=True)
Seeds = np.load(Folder+'Seed0.npy',allow_pickle=True)
for i in range(1,20):
    #Ell0s = np.append(Ell0s,np.load(Folder+'Ell0'+str(i)+'.npy',allow_pickle=True))
    Gammas = np.append(Gammas,np.load(Folder+'Gamma'+str(i)+'.npy',allow_pickle=True))
    Lines = np.append(Lines,np.load(Folder+'Line'+str(i)+'.npy',allow_pickle=True),axis=0)
    Seeds = np.append(Seeds,np.load(Folder+'Seed'+str(i)+'.npy',allow_pickle=True))

Folder = 'ellmin5_Wmax10_Nmax100_dGamma100_second_batch/'
#Ell0s = np.load(Folder+'Ell00.npy',allow_pickle=True)
#Gammas = np.load(Folder+'Gamma0.npy',allow_pickle=True)
#Lines = np.load(Folder+'Line0.npy',allow_pickle=True)
#Seeds = np.load(Folder+'Seed0.npy',allow_pickle=True)
for i in range(0,100):
    Ell0s = np.append(Ell0s,np.load(Folder+'Ell0'+str(i)+'.npy',allow_pickle=True))
    Gammas = np.append(Gammas,np.load(Folder+'Gamma'+str(i)+'.npy',allow_pickle=True))
    Lines = np.append(Lines,np.load(Folder+'Line'+str(i)+'.npy',allow_pickle=True),axis=0)
    Seeds = np.append(Seeds,np.load(Folder+'Seed'+str(i)+'.npy',allow_pickle=True))

for n,line in enumerate(Lines):
    Lines[n][np.where(line==919)] = 0
print('Ell0s')
print('Gammas')
print('Lines')
print('Seeds')

def sort_arrays_according_to_first_one(*arg):
    res = list()
    for array in arg[:]:
        NewArray = copy.copy(array)
        NewArray = array[arg[0].argsort()]
        res.append(NewArray)
    return res

def bin_datas(Nbins,X_array,Y_array):
    #Bins the fraction[:,1]
    BinMin=min(X_array)
    BinMax = max(X_array)
    Y_binned_array = np.zeros((Nbins,2),dtype=float)
    #print(NuBinned.shape)
    for n,Y in enumerate(Y_array):
        Y_binned_array[int((X_array[n]-BinMin)/(BinMax-BinMin)*(Nbins-1)),0] +=Y
        Y_binned_array[int((X_array[n]-BinMin)/(BinMax-BinMin)*(Nbins-1)),1] +=1
    Y_binned_array[:,0] = np.nan_to_num(Y_binned_array[:,0]/Y_binned_array[:,1],0)
    Y_binned_array[:,0] = Y_binned_array[:,0]/sum(Y_binned_array[:,0])
    return Y_binned_array
