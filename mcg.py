#!/usr/bin/env python

"""
MODFLOW 96 Case Generation (Python)
MCG.PY
v.1.1.0
By John Gentle
Updated 2016.07.01

Python script to prepare case scenario input files for use in MODFLOW 96.
See README for usage instructions.
"""

####################################################################
# Custom script to generate a modflow 96 case (scenario).
# Makes a case set for each recharge interpretation with each well scalar.
# Expects a directory path containing all the common base model files.
# Expects a directory path containing all the recharge interpretation files.
# Expects a directory path containing all the wells scalar files.
# Optionally takes a custom output control config file.
####################################################################

####################################################################
# Imports.
####################################################################

# import sys, inspect
import os
import argparse
import shutil

####################################################################
# Testing.  !!!! REMOVE WHEN DEV IS COMPLETED !!!!
####################################################################

# print 'sys.argv[0]: ', sys.argv[0]                  # sys.argv[0] will always contain the name of the script, exactly as it appears on the command line.
# pathname = os.path.dirname(sys.argv[0])             # If the given filename does not include any path information, os.path.dirname returns an empty string.
# print 'path: ', pathname                            # empty string
# print 'full path: ', os.path.abspath(pathname)      # takes a pathname, which can be partial or even blank, and returns a fully qualified pathname.

####################################################################
# Arguments Parser
####################################################################

# ARGUMENTS CONFIG
__author__ = 'jgentle'
parser = argparse.ArgumentParser(description='This is the mcg.py MODFLOW 96 case generation script.')

# note: set required to false in order to use set_defaults on an option.
parser.add_argument('-msd', '--modelsourcedir', help='Input directory path for the model source data. Defaults to model_src if no argument is provided.', required=False)
parser.add_argument('-rd', '--rechargedir', help='Input directory path for the recharge interpretation source files. Defaults to recharge_interpretations if no argument is provided.', required=False)
parser.add_argument('-wd', '--welldir', help='Input directory path for the well scalar source files. Defaults to well_scalars if no argument is provided.', required=False)
parser.add_argument('-mf', '--manifestfile', help='Filename for the manifest to track generated cases. Defaults to scenario_manifest.dat if no argument is provided.', required=False)
parser.add_argument('-od', '--outputdir', help='Output directory for the generated cases. Defaults to generated_cases if no argument is provided.', required=False)
parser.add_argument('-cp', '--caseprefix', help='Naming prefix for the generated case directories. Defaults to case if no argument is provided.', required=False)
parser.add_argument('-dr', '--dryrun', help='Dry run the script without generating cases to test configs. Defaults to false if no argument is provided.', required=False)


# Set some defaults for simplicity.
parser.set_defaults(modelsourcedir="model_src") # ./
parser.set_defaults(rechargedir="recharge_interpretations")  # ./
parser.set_defaults(welldir="well_scalars")# ./
parser.set_defaults(manifestfile="scenario_manifest.dat")
parser.set_defaults(outputdir="generated_cases")# ./
parser.set_defaults(caseprefix="case")
parser.set_defaults(dryrun='false')

# Parse the cli args (which will supercede the defaults).
args = parser.parse_args()

####################################################################
# Variables.
####################################################################

# current_dir = os.path.abspath('')
current_dir = os.getcwd()

# model_src_dir = './base_model_src'
model_src_dir = args.modelsourcedir
model_src_path = os.path.abspath(model_src_dir)

# recharge_dir = './recharge_interpretations'
recharge_dir = args.rechargedir
recharge_path = os.path.abspath(recharge_dir)

# well_dir = './well_scalars'
well_dir = args.welldir
well_path = os.path.abspath(well_dir)

# manifest_file = 'scenario_manifest.dat'
manifest_file = args.manifestfile
manifest_file_target = current_dir + '/' + manifest_file

# generated_cases_dir = 'generated_cases'
generated_cases_dir = args.outputdir
generated_cases_path = os.path.abspath(generated_cases_dir)

# generated_cases_prefix = '/bsgam_mf96_'
generated_cases_prefix = '/' + args.caseprefix + '_'

dry_run = args.dryrun

####################################################################
# Methods.
####################################################################

# LOG ARGUMENTS
def logArguments():
    print ("mcg.py module arguments:")
    print ("-------------------------------")
    # print ("First argument: %s" % str(sys.argv[1]))
    # print ("Second argument: %s" % str(sys.argv[2]))
    # print ("Third argument: %s" % str(sys.argv[3]))
    # for i in xrange(total):
    #     print ("Argument # %d : %s" % (i, str(sys.argv[i])))
    # print ("The total numbers of args passed to the script: %d" % total)
    # print ("Args list: %s" % cmdargs)
    print (" ")
    return

# LOG PARSER ARGS
def logArgsParser():
    print ("mcg.py script arguments:")
    print ("-------------------------------")
    print ("Model source directory: %s" % args.modelsourcedir)
    print ("Recharge interpretations directory: %s" % args.rechargedir)
    print ("Well scalars directory: %s" % args.welldir)
    print ("Manifest file: %s" % args.manifestfile)
    print ("Generated cases output directory: %s" % args.outputdir)
    print ("Prefix for generated case folders: %s" % args.caseprefix)
    print (" ")
    return

# LOG VARIABLES
def logVariables():
    print ("mcg.py script variables:")
    print ('--------------------------------------')
    print ('current_dir: %s' % current_dir)
    print ('model_src_dir: %s' % model_src_dir)
    print ('model_src_path: %s' % model_src_path)
    print ('recharge_dir: %s' % recharge_dir)
    print ('recharge_path: %s' % recharge_path)
    print ('well_dir: %s' % well_dir)
    print ('well_path: %s' % well_path)
    print ('manifest_file: %s' % manifest_file)
    print ('manifest_file_target: %s' % manifest_file_target)
    print ('generated_cases_dir: %s' % generated_cases_dir)
    print ('generated_cases_path: %s' % generated_cases_path)
    print ('generated_cases_prefix: %s' % generated_cases_prefix)
    print ('dry_run: %s' % dry_run)
    print (' ')

# TRACK CASE GENERATION
def appendToManifest(manifest_entry):
    print '--------------------------------------'
    # print 'Opening manifest file...'
    scenario_manifest = open(manifest_file, 'a+')
    # print '- Name of the scenario_manifest file: ', scenario_manifest.name
    # print '- Closed or not (scenario_manifest): ', scenario_manifest.closed
    # print '- Opening mode (scenario_manifest): ', scenario_manifest.mode
    # print '- Softspace flag (scenario_manifest): ', scenario_manifest.softspace
    # print ' '
    print 'Appending manifest file with:'
    print '- manifest_entry:\n', manifest_entry
    scenario_manifest.write(manifest_entry + '\n')
    print 'Manifest file updated with current scenario.'
    # print ' '
    # print 'Closing manifest file...'
    scenario_manifest.close()
    # print '- Name of the scenario_manifest file: ', scenario_manifest.name
    # print '- Closed or not (scenario_manifest): ', scenario_manifest.closed
    # print '... manifest file closed.'
    print ' '

# CLEAR HISTORY
def deleteManifest():
    print '--------------------------------------'
    if (os.path.isfile(manifest_file_target)):
        print '- Manifest file found...'
        os.remove(manifest_file_target)
        print '- Manifest file deleted.'
    else:
        print '- No manifest file found.'
    print ' '


####################################################################
# Generation Logic.
####################################################################

def generateScenarios():
    print ' '
    print '--------------------------------------'
    print 'Starting Modflow 96 Case Generation...'
    print '--------------------------------------'
    print ' '

    deleteManifest()

    # Iterate over recharge interpretations.
    for recharge_interpretation in os.listdir(recharge_path):
        # Iterate over well scalars.
        for well_scenario in os.listdir(well_path):
            print '============================================'
            print 'Generating new case from:'
            print '- recharge_interpretation: ', recharge_interpretation
            print '- well_scenario: ', well_scenario
            print ' '

            # Script filename (usually with path)
            #print inspect.getfile(inspect.currentframe())
            # Script directory
            #print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
            #print os.path.splitext(wel_)[0]

            # Build directory name for case.
            current_scenario_dir = generated_cases_dir + generated_cases_prefix \
                + os.path.splitext(recharge_interpretation)[0] \
                + '_' + os.path.splitext(well_scenario)[0]
            #print '- current_scenario_dir: ', current_scenario_dir

            # Create directory if it does not exist.
            if not os.path.exists(current_scenario_dir):
                os.makedirs(current_scenario_dir)

            # Create references to source files.
            current_scenario_destdir = current_dir + '/' + current_scenario_dir
            recharge_interpretation_file = recharge_path + '/' + recharge_interpretation
            well_scalar_file = well_path + '/' + well_scenario
            #print '- current_scenario_destdir: ', current_scenario_destdir
            #print '- recharge_interpretation_file: ', recharge_interpretation_file
            #print '- well_scalar_file: ', well_scalar_file

            # Copy model base files into current scenario directory..
            model_src_files = os.listdir(model_src_path)
            for src_file in model_src_files:
                model_src_file_path = os.path.join(model_src_path, src_file)
                if (os.path.isfile(model_src_file_path)):
                    shutil.copy(model_src_file_path, current_scenario_destdir)

            # Copy current recharge interpretation into current scenario directory and rename to rch.dat.
            shutil.copy(recharge_interpretation_file, current_scenario_destdir)
            recharge_interpretation_file_src = current_scenario_destdir + '/' + recharge_interpretation
            recharge_interpretation_file_target = current_scenario_destdir + '/rch.dat'
            #print '- recharge_interpretation_file_src: ', recharge_interpretation_file_src
            #print '- recharge_interpretation_file_target: ', recharge_interpretation_file_target
            os.rename(recharge_interpretation_file_src, recharge_interpretation_file_target)

            # Copy current well scalars into current scenario directory and rename to wel.dat.
            shutil.copy(well_scalar_file, current_scenario_destdir)
            well_scalar_file_src = current_scenario_destdir + '/' + well_scenario
            well_scalar_file_target = current_scenario_destdir + '/wel.dat'
            #print '- well_scalar_file_src: ', well_scalar_file_src
            #print '- well_scalar_file_target: ', well_scalar_file_target
            os.rename(well_scalar_file_src, well_scalar_file_target)

            # Copy custom output control file into current scenario directory and rename to oc.dat.
            # TBD

            # Append current scenario directory to scenario manifest file.
            appendToManifest(current_scenario_dir)

    print ' '
    print '--------------------------------------'
    print 'Modflow 96 Case Generation Complete.'
    print '--------------------------------------'
    print ' '

####################################################################
# Start Module.
####################################################################

# logArguments()
logArgsParser()
logVariables()

if dry_run == 'true':
    # sys.exit(0)
    quit()
else:
    generateScenarios()

####################################################################
# End Module.
####################################################################