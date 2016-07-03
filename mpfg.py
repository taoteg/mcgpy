#!/usr/bin/env python

"""
MODFLOW 96 Parameters File Generation (Python)
MPFG.PY
v.1.1.0
By John Gentle
Updated 2016.07.03

Python script to prepare case scenario input files for use in MODFLOW 96.
See README for usage instructions.
"""

####################################################################
# Imports.
####################################################################
import os


####################################################################
# Variables.
####################################################################
iterator = 0
maxIterations = 80
casePrefix = 'bsgam_mf96'
taskCount = '240'
manifest_file = 'mpfg.mcg.' + taskCount + '.paramlist'
manifest_file_target = os.getcwd() + '/' + manifest_file
rechargePath = './recharge_interpretations/'
wellsPath = './parameterized_well_scalars/'


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


def appendToManifest(manifest_entry):
    scenario_manifest = open(manifest_file, 'a+')
    scenario_manifest.write(manifest_entry + '\n')
    scenario_manifest.close()


####################################################################
# Start Module.
####################################################################
scriptStatus('>>> Generating Params...')

# for recharge in os.listdir(rechargePath):
for recharge in listdir_nohidden(rechargePath):

    rechargeFile = os.path.splitext(recharge)[0]
    rechargeTarget = rechargePath + rechargeFile    #+ '.dat'
    print rechargeTarget
    # quit()

    while (iterator < maxIterations):
        # wellsPath = '/parameterized_well_scalars/wells_group_' + str(iterator)
        wellsFile = 'wells_group_' + str(iterator)
        wellsTarget = wellsPath + wellsFile

        manifestTitle = 'manifest_' + rechargeFile + '_wells_group_' + str(iterator) + '.dat'
        current_param = "python mcg.py -rd \"" + rechargeTarget + "\" -wd \"" + wellsTarget + "\" -mf \"" + manifestTitle + "\" -cp \"" + casePrefix + "\""
        print 'current_param: ', current_param
        appendToManifest(current_param)
        iterator = iterator + 1
        print 'iterator: ', iterator
    else:
        scriptStatus('...Params Generated <<<')
        iterator = 0
        
quit()

####################################################################
# End Module.
####################################################################