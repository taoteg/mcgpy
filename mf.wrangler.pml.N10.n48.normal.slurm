#!/bin/bash
#
# Simple SLURM script for submitting multiple serial
# jobs (e.g. parametric studies) using a script wrapper
# to launch the jobs.
#
# To use, build the launcher executable and your
# serial application(s) and place them in your WORKDIR
# directory.  Then, edit the CONTROL_FILE to specify
# each executable per process.
#-------------------------------------------------------
#-------------------------------------------------------
#
#------------------Scheduler Options--------------------
#SBATCH -J MF96_BSGAM_Cases         # Job name
#SBATCH -N 10                       # Total number of nodes (24 cores/node)
#SBATCH -n 48                       # Total number of tasks (Actually cores in parametric launcher. Usually 24, but can try 48 on wrangler with hyperthreading on)
#SBATCH -p normal                   # Queue name (normal, hadoop, dev)
#SBATCH -o Parametric.o_%j          # Name of stdout output file (%j expands to jobid)
#SBATCH -t 48:00:00                 # Run time (hh:mm:ss)
#
# <------------ Account String ------------>
# <--- (Use this ONLY if you have MULTIPLE accounts) --->
#SBATCH -A Groundwater-Decision
#   
#------------------------------------------------------
#
# Usage:
#   #$ -pe <parallel environment> <number of slots>
#   #$ -l h_rt=hours:minutes:seconds to specify run time limit
#   #$ -N <job name>
#   #$ -q <queue name>
#   #$ -o <job output file>
#      NOTE: The env variable $JOB_ID contains the job id.
#
#------------------General Options---------------------
module load launcher
# module load python

export TACC_LAUNCHER_PPN=24
export EXECUTABLE=$TACC_LAUNCHER_DIR/init_launcher
export WORKDIR=.
export CONTROL_FILE=mf.96.cases.sorted.paramlist

# Variable descriptions:
#
#  TACC_LAUNCHER_PPN = number of simultaneous processes per host
#                      - if this variable is not set, value is
#                        determined by the process density/wayness
#                        specified in 'Scheduler Options'
#  EXECUTABLE        = full path to the job launcher executable
#  WORKDIR           = location of working directory
#  CONTROL_FILE      = text input file which specifies
#                      executable for each process
#                      (should be located in WORKDIR)
#------------------------------------------------------

#--------- Intel Xeon Phi Options (EXPERIMENTAL) -------------
export TACC_LAUNCHER_NPHI=0
export TACC_LAUNCHER_PHI_PPN=8
export PHI_WORKDIR=.
export PHI_CONTROL_FILE=phiparamlist

# Variable descriptions:
#  TACC_LAUNCHER_NPHI    = number of Intel Xeon Phi cards to use per node
#                          (use 0 to disable use of Xeon Phi cards)
#  TACC_LAUNCHER_PHI_PPN = number of simultaneous processes per Xeon Phi card
#  PHI_WORKDIR           = location of working directory for Intel Xeon Phi jobs
#  PHI_CONTROL_FILE      = text input file which specifies executable
#                          for each process to be run on Intel Xeon Phi
#                          (should be located in PHI_WORKDIR)
#------------------------------------------------------

#------------ Task Scheduling Options -----------------
export TACC_LAUNCHER_SCHED=interleaved

# Variable descriptions:
#  TACC_LAUNCHER_SCHED = scheduling method for lines in CONTROL_FILE
#                        options (k=process, n=num. lines, p=num. procs):
#                          - interleaved (default):
#                              process k executes every k+nth line
#                          - block:
#                              process k executes lines [ k(n/p)+1 , (k+1)(n/p) ]
#                          - dynamic:
#                              process k executes first available unclaimed line
#--------------------------------------------------------

#----------------
# Error Checking
#----------------

if [ ! -d $WORKDIR ]; then
        echo " "
    echo "Error: unable to change to working directory."
    echo "       $WORKDIR"
    echo " "
    echo "Job not submitted."
    exit
fi

if [ ! -x $EXECUTABLE ]; then
    echo " "
    echo "Error: unable to find launcher executable $EXECUTABLE."
    echo " "
    echo "Job not submitted."
    exit
fi

if [ ! -e $WORKDIR/$CONTROL_FILE ]; then
    echo " "
    echo "Error: unable to find input control file $CONTROL_FILE."
    echo " "
    echo "Job not submitted."
    exit
fi

#----------------
# Job Submission
#----------------

cd $WORKDIR/
echo " WORKING DIR:   $WORKDIR/"

$TACC_LAUNCHER_DIR/paramrun SLURM $EXECUTABLE $WORKDIR $CONTROL_FILE $PHI_WORKDIR $PHI_CONTROL_FILE

echo " "
echo " Parametric Job Complete"
echo " "