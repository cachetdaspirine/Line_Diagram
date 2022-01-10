#!/bin/bash
SimMax=99


# create a directory with a new number
i=0
# while the directory (-d) exist, use a higher number
while [ -d Res_$i ];do
	let i+=1
done
#this is the name of the directory
FileName=Res_$i
#make the directory
mkdir $FileName

for SimNum in $(seq 0 $SimMax)
do
	sbatch Submit_High_L_Matrix.pbs $SimNum $SimMax $FileName
	#bash Submit_High_L_Matrix.pbs $SimNum $SimMax $FileName
done
