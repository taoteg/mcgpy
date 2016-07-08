#!/usr/bin/env python

"""
MODFLOW 96 Case Parameters File Generation (Python)
MCPFG.PY
v.1.1.0
By John Gentle
Updated 2016.07.03

Python script to generate the paramlist file for case scenario inputs used in MODFLOW 96.
See README for usage instructions.
"""

# Get list of case dirs to iterate over.
#   List could be generated from:
#       - a file,
#       - run on the node with a ref to hte actual case dirs,
#       - run from within the target dirs parent.
# For each dir in list, generate command:
#   cd /target/dir/path && mf96
# Append command to paramlist
# Will result in as many lines as there are case scenarios.

####################################################################
# Imports.
####################################################################
import os


####################################################################
# Variables.
####################################################################
scenario_dirs_path = '/data/03325/jgentle/encompass/modflow/modflow96/data_src/generated_cases/bsgam/gen_2'
# scenario_dirs_name = 'gen_2'
scenario_dirs_name = os.getcwd()
scenario_dirs_target = os.path.abspath(scenario_dirs_name)

paramlist_prefix = 'mf.96'
paramlist_label = 'cases.sorted'
paramlist_file = paramlist_prefix + '.' + paramlist_label + '.paramlist'
paramlist_file_target = os.getcwd() + '/' + paramlist_file


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


def appendToParamlist(new_entry):
    scenario_paramlist = open(paramlist_file, 'a+')
    scenario_paramlist.write(new_entry + '\n')
    scenario_paramlist.close()


####################################################################
# Start Module.
####################################################################
scriptStatus('>>> Generating Case Params...')

# case_dirs = sorted(listdir_nohidden(scenario_dirs_target))
# print 'case_dirs: ', case_dirs

for case in case_dirs:
    # print 'case: ', case
    current_param = "cd " + os.getcwd() + "/" + case + " && mf96"
    # print 'current_param: ', current_param

    appendToParamlist(current_param)

scriptStatus('...Case Params Generated <<<')
quit()


####################################################################
# End Module.
####################################################################
