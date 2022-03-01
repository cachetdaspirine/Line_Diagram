#!/bin/bash
SimMax=10
SEEDFILE=last_max_seed.txt
<<<<<<< HEAD
Nparticles=100
=======
Nparticles=100000
#start by loading python :
module load gcc/8.4.0 python/3.7.7
>>>>>>> 2dc1f3b4a07cc1462883ad1e9949423b19619b6b
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
# check if the seed file exists
if ! test -f "$SEEDFILE"; then
    0 > $SEEDFILE
fi

for SimNum in $(seq 0 $SimMax)
do
	# get the correct seed
	SEED=$(< $SEEDFILE)
	SEED=$(($SEED + $Nparticles))
	echo $SEED > $SEEDFILE
<<<<<<< HEAD
	#sbatch Submit_High_L_Matrix.pbs $SimNum $SimMax $FileName $SEED
	python3 Loop_For_High_L.py $SimNum $SimMax $FileName $SEED &
=======
	sbatch Submit_High_L_Matrix.pbs $SimNum $SimMax $FileName $SEED $Nparticles
	#python3 Loop_For_High_L.py $SimNum $SimMax $FileName $SEED &
>>>>>>> 2dc1f3b4a07cc1462883ad1e9949423b19619b6b
	echo $SimNum
done
