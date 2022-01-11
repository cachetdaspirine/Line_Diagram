#!/bin/bash
SimMax=99


dir_name=ellmin5_Wmax10_Nmax100_dGamma100_second_batch

for SimNum in $(seq 0 $SimMax)
do
	sbatch submit_best_aggregate.pbs $SimNum $dir_name
	#bash submit_best_aggregate.pbs $SimNum $dir_name
done
