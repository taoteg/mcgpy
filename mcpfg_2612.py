#!/usr/bin/env python

"""
MODFLOW 96 Case Parameters File Generation (Python)
Variant for 2612 Candidate Solutions with Springflow Delta >= 3 cfs

MCPFG.PY
v.1.1.0
By John Gentle
Updated 2016.07.03

Python script to generate the paramlist file for
case scenario inputs used in MODFLOW 96.
See README for usage instructions.
"""

# WORKFLOW:
# Get list of candidate case hashes from csv file.
# Generate multiple paramlist for the cases (in 240 case groups).
# Generate multiple slurm scripts (one for each of the paramlist files).
# Run slurm scripts for cases.
# Copy cases to Stampede for group access.
# Split data paramlist into chunks using this command:
#   $ split -a 3 -l 240 candidate_paramlist_all.dat candidate.paramlist.chunk.
# Create a new slurm script that uses each paramlist chunk.
# Run each slurm script manually on HPC (for now).

####################################################################
# Imports.
####################################################################
import os


####################################################################
# Variables.
####################################################################
candidate_run_hashes_dir = 'candidate_runs/'
candidate_run_hashes_src = 'candidate_hashes_drain_delta_gt3_hashOnly.csv'
candidate_run_target = candidate_run_hashes_dir + candidate_run_hashes_src
candidate_run_path = '/data/03325/jgentle/encompass/modflow/modflow96/data_src/generated_cases/bsgam/gen_2/'
case_dirame_prefix = 'bsgam_mf96_'
case_dirname_midfix = '_wells_'
rchType = ['rchTRBAR', 'rchTRMAC', 'rchTRNEW', 'rchTROLD']
paramlist_file = 'candidate_paramlist_all.dat'

# print candidate_run_hashes_dir
# print candidate_run_hashes_src
# print candidate_run_path
# print case_dirame_prfix
# print case_dirname_midfix
# print rchType
# print paramlist_file


####################################################################
# Methods.
####################################################################
def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f


def scriptStatus(scriptState):
    print '-----------------------------------'
    print '%s' % scriptState
    print '-----------------------------------'
    print ' '


# CLEAR HISTORY
def deleteParamlist():
    print '--------------------------------------'
    if (os.path.isfile(paramlist_file_target)):
        print '- Paramlist file found...'
        os.remove(paramlist_file_target)
        print '- Paramlist file deleted.'
    else:
        print '- No paramlist file found.'
    print ' '


def appendToParamlist(new_entry):
    scenario_paramlist = open(paramlist_file, 'a+')
    scenario_paramlist.write(new_entry + '\n')
    scenario_paramlist.close()


####################################################################
# Derived Variables.
####################################################################
current_dir = os.getcwd()
# current_dir_path = os.path.abspath(current_dir)
# candidate_run_hashes_path = os.path.abspath(candidate_run_hashes_dir)
candidate_runs = listdir_nohidden(candidate_run_path)
paramlist_file_target = current_dir + '/' + paramlist_file

print candidate_runs

####################################################################
# Start Module.
####################################################################
scriptStatus('>>> Generating Case Params...')

deleteParamlist()

for rch in rchType:
    with open(candidate_run_target) as candidates:
        for hashcode in candidates:
            # print 'rch: ', rch
            # print 'hashcode: ', hashcode
            # clean the hash
            hashcode_clean = hashcode.rstrip('\n')
            # create the new case target path.
            case_dirname = case_dirame_prefix
            case_dirname += rch
            case_dirname += case_dirname_midfix
            case_dirname += hashcode_clean
            # print 'case_dirname: ', case_dirname
            # create the new paramlist argument.
            current_param = "cd "
            current_param += candidate_run_path
            current_param += case_dirname
            current_param += " && mf96"
            # print current_param
            # append the new argument to the paramlist file.
            appendToParamlist(current_param)

scriptStatus('...Case Params Generated <<<')
quit()

####################################################################
# End Module.
####################################################################
