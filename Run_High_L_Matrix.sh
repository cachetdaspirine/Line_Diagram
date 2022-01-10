#!/bin/bash
SimMax=5


# create a directory with a new number
i=0
while [ -d Res_$i ];do
	let i+=1
done

FileName=Res_$i

mkdir $FileName

for SimNum in $(seq 0 $SimMax)
do
	#sbatch Submit.pbs $SimNum $SimMax $FileName
	bash Submit_High_L_Matrix.pbs $SimNum $SimMax $FileName
done
