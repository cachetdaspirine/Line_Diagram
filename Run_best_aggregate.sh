#!/bin/bash
SimMax=99
#NparticlesTotal=2900
NparticlesTotal=500

#module load gcc/8.4.0 python/3.7.7

#dir_name=ellmin5_Wmax10_Nmax100_dGamma100_second_batch
dir_name=gamma_ell0
file_name=top_ell_homogeneous_nu_

for SimNum in $(seq 0 $SimMax)
do
	#sbatch -W submit_best_aggregate.pbs $SimNum $SimMax $dir_name $file_name $NparticlesTotal &
	python3 loop_best_aggregate.py $SimNum $SimMax $dir_name $file_name $NparticlesTotal &
done;
#wait

date

#python3 merge_data.py $SimMax $dir_name
