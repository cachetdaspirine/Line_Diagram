This simulation contain several parts :


High_L_Matrix Simulations :
---------------------------

Runs on cluster with :
$ ./Run_High_L_Matrix.sh

it will first run a bash script that creates a folder with a new number to not
over write previous simulation results. This folder will contain all the simu-
-ation results. Then it runs a loop of Submit_High_L_Matrix.pbs scrip, each o-
-f them runs a separate simulation to find matrix with high L value. Each of
these simulation writes in its own file, but open all the other output files
to keep a shared track of the seeds compute. This should avoid as much as pos-
-sible overlapping seeds. while avoiding writting simultaneously in a file.
