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

# Get ref to list of case dirs to iterate over.
#   List could be generated from a file,
#   or run on node with ref to actual case dirs,
#   or run form within target dirs parent.
# For each dir in list, generate command:
#       cd /target/dir/path && mf96
# Append command to paramlist
# Will result in as any lines as there are case scenarios.

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


# def appendToManifest(manifest_entry):
#     scenario_manifest = open(manifest_file, 'a+')
#     scenario_manifest.write(manifest_entry + '\n')
#     scenario_manifest.close()


####################################################################
# Start Module.
####################################################################
scriptStatus('>>> Generating Case Params...')

for case_dir in listdir_nohidden(scenario_dirs_target):
    print case_dir


quit()
####################################################################
# End Module.
####################################################################
