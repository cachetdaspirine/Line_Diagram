import numpy as np
import copy
########################## ellmin5 to infinity####################
# Folder = 'ellmin5_Wmax10_Nmax100_dGamma100_first_batch/'
# Ell0s = np.load(Folder+'Ell00.npy',allow_pickle=True)
# Gammas = np.load(Folder+'Gamma0.npy',allow_pickle=True)
# Lines = np.load(Folder+'Line0.npy',allow_pickle=True)
# Seeds = np.load(Folder+'Seed0.npy',allow_pickle=True)
# for i in range(1,20):
#     #Ell0s = np.append(Ell0s,np.load(Folder+'Ell0'+str(i)+'.npy',allow_pickle=True))
#     Gammas = np.append(Gammas,np.load(Folder+'Gamma'+str(i)+'.npy',allow_pickle=True))
#     Lines = np.append(Lines,np.load(Folder+'Line'+str(i)+'.npy',allow_pickle=True),axis=0)
#     Seeds = np.append(Seeds,np.load(Folder+'Seed'+str(i)+'.npy',allow_pickle=True))
#
# Folder = 'ellmin5_Wmax10_Nmax100_dGamma100_second_batch/'
# for i in range(0,100):
#     Ell0s = np.append(Ell0s,np.load(Folder+'Ell0'+str(i)+'.npy',allow_pickle=True))
#     Gammas = np.append(Gammas,np.load(Folder+'Gamma'+str(i)+'.npy',allow_pickle=True))
#     Lines = np.append(Lines,np.load(Folder+'Line'+str(i)+'.npy',allow_pickle=True),axis=0)
#     Seeds = np.append(Seeds,np.load(Folder+'Seed'+str(i)+'.npy',allow_pickle=True))


########################## ellmin3 to ellmax5####################
#Folder = 'result_by_simulating_the_whole_aggregates/ellmin3_ellmax5/'
# Folder = 'result_by_simulating_the_whole_aggregates/ellmin0_ellmax3/'
# Ell0s = np.load(Folder+'Ell00.npy',allow_pickle=True)
# Gammas = np.load(Folder+'Gamma0.npy',allow_pickle=True)
# Lines = np.load(Folder+'Line0.npy',allow_pickle=True)
# Seeds = np.load(Folder+'Seed0.npy',allow_pickle=True)
# for i in range(1,10):
#     Ell0s = np.append(Ell0s,np.load(Folder+'Ell0'+str(i)+'.npy',allow_pickle=True))
#     Gammas = np.append(Gammas,np.load(Folder+'Gamma'+str(i)+'.npy',allow_pickle=True))
#     Lines = np.append(Lines,np.load(Folder+'Line'+str(i)+'.npy',allow_pickle=True),axis=0)
#     Seeds = np.append(Seeds,np.load(Folder+'Seed'+str(i)+'.npy',allow_pickle=True))
########################## Strips top 10e6 ell####################
Folder_top = 'result_by_simulating_strips/centralized_data/final_res_top_ell/'
Ell0s_top = np.load(Folder_top+'Ell00.npy',allow_pickle=True)
Gammas_top = np.load(Folder_top+'Gamma0.npy',allow_pickle=True)
Lines_top = np.load(Folder_top+'Line0.npy',allow_pickle=True)
Seeds_top = np.load(Folder_top+'Seed0.npy',allow_pickle=True)
try:
    NUs_top = np.load(Folder_top+'NUs.npy')
except FileNotFoundError:
    print('No Nu_top')
print('Ell0s_top')
print('Gammas_top')
print('Lines_top')
print('Seeds_top')
print('NUs_top')
print()
for i in range(1,100):
    Ell0s_top = np.append(Ell0s_top,np.load(Folder_top+'Ell0'+str(i)+'.npy',allow_pickle=True))
    Gammas_top = np.append(Gammas_top,np.load(Folder_top+'Gamma'+str(i)+'.npy',allow_pickle=True))
    Lines_top = np.append(Lines_top,np.load(Folder_top+'Line'+str(i)+'.npy',allow_pickle=True),axis=0)
    Seeds_top = np.append(Seeds_top,np.load(Folder_top+'Seed'+str(i)+'.npy',allow_pickle=True))
    
#for n,line in enumerate(Lines_top):
#    Lines_top[n][np.where(line==919)] = 0

########################## Strips intermediate 10e6 ell####################
Folder_int = 'result_by_simulating_strips/centralized_data/final_res_int_ell/'
Ell0s_int = np.load(Folder_int+'Ell00.npy',allow_pickle=True)
Gammas_int = np.load(Folder_int+'Gamma0.npy',allow_pickle=True)
Lines_int = np.load(Folder_int+'Line0.npy',allow_pickle=True)
Seeds_int = np.load(Folder_int+'Seed0.npy',allow_pickle=True)
try:
    NUs_int = np.load(Folder_int+'NUs.npy')
except FileNotFoundError:
    print('No Nu_int')
print('Ell0s_int')
print('Gammas_int')
print('Lines_int')
print('Seeds_int')
print('NUs_int')
print()
for i in range(1,100):
    Ell0s_int = np.append(Ell0s_int,np.load(Folder_int+'Ell0'+str(i)+'.npy',allow_pickle=True))
    Gammas_int = np.append(Gammas_int,np.load(Folder_int+'Gamma'+str(i)+'.npy',allow_pickle=True))
    Lines_int = np.append(Lines_int,np.load(Folder_int+'Line'+str(i)+'.npy',allow_pickle=True),axis=0)
    Seeds_int = np.append(Seeds_int,np.load(Folder_int+'Seed'+str(i)+'.npy',allow_pickle=True))
#for n,line in enumerate(Lines_int):
#    Lines_int[n][np.where(line==919)] = 0

########################## Strips bottom 10e6 ell####################    
Folder_low='result_by_simulating_strips/centralized_data/final_res_low_ell/'
Ell0s_low = np.load(Folder_low+'Ell00.npy',allow_pickle=True)
Gammas_low = np.load(Folder_low+'Gamma0.npy',allow_pickle=True)
Lines_low = np.load(Folder_low+'Line0.npy',allow_pickle=True)
Seeds_low = np.load(Folder_low+'Seed0.npy',allow_pickle=True)
try:
    NUs_low = np.load(Folder_low+'NUs.npy')
except FileNotFoundError:
    print('No Nu_low')
print('Ell0s_low')
print('Gammas_low')
print('Lines_low')
print('Seeds_low')
print('NUs_low')
for i in range(1,100):
    Ell0s_low = np.append(Ell0s_low,np.load(Folder_low+'Ell0'+str(i)+'.npy',allow_pickle=True))
    Gammas_low = np.append(Gammas_low,np.load(Folder_low+'Gamma'+str(i)+'.npy',allow_pickle=True))
    Lines_low = np.append(Lines_low,np.load(Folder_low+'Line'+str(i)+'.npy',allow_pickle=True),axis=0)
    Seeds_low = np.append(Seeds_low,np.load(Folder_low+'Seed'+str(i)+'.npy',allow_pickle=True))
#for n,line in enumerate(Lines_low):
#    Lines_low[n][np.where(line==919)] = 0
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
