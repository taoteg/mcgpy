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
import shutil

####################################################################
# Testing.  !!!! REMOVE WHEN DEV IS COMPLETED !!!!
####################################################################

# print 'sys.argv[0]: ', sys.argv[0]                  # sys.argv[0] will always contain the name of the script, exactly as it appears on the command line.
# pathname = os.path.dirname(sys.argv[0])             # If the given filename does not include any path information, os.path.dirname returns an empty string.
# print 'path: ', pathname                            # empty string
# print 'full path: ', os.path.abspath(pathname)      # takes a pathname, which can be partial or even blank, and returns a fully qualified pathname.

####################################################################
# Variables.
####################################################################
# current_dir = os.path.abspath('')
current_dir = os.getcwd()
model_src_dir = './bsgam_base_model'
model_src_path = os.path.abspath(model_src_dir)
recharge_dir = './recharge_interpretations'
recharge_path = os.path.abspath(recharge_dir)
well_dir = './well_scalars'
well_path = os.path.abspath(well_dir)
manifest_file = 'scenario_manifest.dat'
manifest_file_target = current_dir + '/' + manifest_file

print '--------------------------------------'
print 'current_dir: ', current_dir
print 'model_src_dir: ', model_src_dir
print 'model_src_path: ', model_src_path
print 'recharge_dir: ', recharge_dir
print 'recharge_path: ', recharge_path
print 'well_dir: ', well_dir
print 'well_path: ', well_path
print 'manifest_file: ', manifest_file
print 'manifest_file_target: ', manifest_file_target
print ' '


####################################################################
# Methods.
####################################################################
def appendToManifest(manifest_entry):
    print '--------------------------------------'
    # print 'Opening manifest file...'
    scenario_manifest = open(manifest_file, 'a+')
    # print '- Name of the scenario_manifest file: ', scenario_manifest.name
    # print '- Closed or not (scenario_manifest): ', scenario_manifest.closed
    # print '- Opening mode (scenario_manifest): ', scenario_manifest.mode
    # print '- Softspace flag (scenario_manifest): ', scenario_manifest.softspace
    # print ' '
    # print 'Appending manifest file...'
    # print '- manifest_entry:\n', manifest_entry
    scenario_manifest.write(manifest_entry + '\n')
    print 'Manifest file updated with current scenario.'
    # print ' '
    # print 'Closing manifest file...'
    scenario_manifest.close()
    # print '- Name of the scenario_manifest file: ', scenario_manifest.name
    # print '- Closed or not (scenario_manifest): ', scenario_manifest.closed
    # print '... manifest file closed.'
    print ' '


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

    for recharge_interpretation in os.listdir(recharge_path):
        for well_scenario in os.listdir(well_path):
            print 'Generating new case from:'
            print '- recharge_interpretation: ', recharge_interpretation
            print '- well_scenario: ', well_scenario
            print ' '

            # Script filename (usually with path)
            #print inspect.getfile(inspect.currentframe())
            # Script directory
            #print os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
            #print os.path.splitext(wel_)[0]

            current_scenario_dir = 'bsgam_mf96_' \
                + os.path.splitext(recharge_interpretation)[0] \
                + '_' + os.path.splitext(well_scenario)[0]
            #print '- current_scenario_dir: ', current_scenario_dir

            if not os.path.exists(current_scenario_dir):
                os.makedirs(current_scenario_dir)

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
# Execute Script.
####################################################################
generateScenarios()
