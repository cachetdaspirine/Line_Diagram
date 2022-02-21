#!/bin/bash
SimMax=10


#dir_name=ellmin5_Wmax10_Nmax100_dGamma100_second_batch
dir_name=ellmin0_ellmax3

for SimNum in $(seq 0 $SimMax)
do
	#sbatch submit_best_aggregate.pbs $SimNum $dir_name
	python3 loop_best_aggregate.py $SimNum $dir_name &
	#bash submit_best_aggregate.pbs $SimNum $dir_name
done
