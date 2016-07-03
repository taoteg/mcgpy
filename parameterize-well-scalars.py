#!/usr/bin/env python

####################################################################
# Imports.
####################################################################
import os
import shutil


####################################################################
# Variables.
####################################################################
wells_src_dir = 'well_scalars'
wells_src_path = os.path.abspath(wells_src_dir)
wells_src_files = os.listdir(wells_src_path)
wells_dest_dir = 'parameterized_well_scalars'
wells_dest_path = os.path.abspath(wells_dest_dir)

groupRange = 80     # 80 groups.
wellRange = 118     # 118 wells per group.
groupCount = 0
wellCount = 0
totalCount = 0
minValue = 0
increment = groupCount + 1
minRange = minValue + ((increment - 1) * wellRange)
maxRange = increment * wellRange
currentWellIndex = totalCount


####################################################################
# Methods.
####################################################################
def scriptStatus(scriptState):
    print '-----------------------------------'
    print '%s' % scriptState
    print '-----------------------------------'
    print ' '


def logConfigs():
    print 'Logging Current Configuration Settings:'
    print ' '
    print 'wells_src_dir: ', wells_src_dir
    print 'wells_src_path: ', wells_src_path
    print 'wells_src_files: ', wells_src_files
    print 'len(wells_src_files): ', len(wells_src_files)
    print 'wells_src_files[1]: ', wells_src_files[1]
    print 'wells_dest_dir: ', wells_dest_dir
    print 'wells_dest_path: ', wells_dest_path
    print ' '


def logVariables():
    print 'Logging Current Variable Settings:'
    print ' '
    print ('increment %s' % increment)
    print ('minRange %s' % minRange)
    print ('maxRange %s' % maxRange)
    print ('The groupCount is: %s' % groupCount)
    print ('The wellCount is: %s' % wellCount)
    print ('The totalCount is: %s' % totalCount)
    print ' '


# def incrementCounters():

####################################################################
# Start Module.
####################################################################
scriptStatus('>>> START GAME <<<')
logConfigs()

while (groupCount < groupRange):

    # Build the directory name for the current case.
    current_group_dir = 'wells_group_' + str(groupCount)
    current_group_dir_path = wells_dest_path + '/' + current_group_dir

    # Create a directory if it does not exist.
    if not os.path.exists(current_group_dir_path):
        os.makedirs(current_group_dir_path)

    # For the next 118 files...
    if (wellCount < wellRange):

        scriptStatus('>>>>> START ITERATION STATE >>>>>')
        logVariables()

        # for wells_src in wells_src_files:
        #     print '----------------------------------------------------------------------------'
        #     current_wells_file = wells_src_path + '/' + wells_src
        #     print ('The current_wells_file is: %s' % current_wells_file)
        #     print ('The current_group_dir_path is: %s' % current_group_dir_path)

        #     # if not (os.path.exists(current_wells_file)):
        #     #     shutil.copy(current_wells_file, current_group_dir_path)
        #     print ('The wellCount is: %s' % wellCount)
        #     wellCount = wellCount + 1

        # Get a reference to the wells file index.
        currentWellIndex = totalCount
        print 'currentWellIndex: ', currentWellIndex
        current_wells_file = wells_src_files[currentWellIndex]          # in prod.
        # current_wells_file = wells_src_files[0]                           # in dev.
        current_wells_file_path = wells_src_path + '/' + current_wells_file
        print 'current_wells_file: ', current_wells_file
        print 'current_wells_file_path: ', current_wells_file_path
        print 'current_group_dir_path: ', current_group_dir_path
        print ' '

        # Check if well file exists...
        if not (os.path.exists(current_wells_file_path)):
            print 'DOES NOT EXIST - current_wells_file_path: ', current_wells_file_path
            print ' '

        # Copy the well file to the current group dir.
        if (os.path.exists(current_wells_file_path)):
            print 'EXISTS - current_wells_file_path: ', current_wells_file_path
            print ' '
            shutil.copy(current_wells_file_path, current_group_dir_path)

        # Increment the counters.
        wellCount = wellCount + 1
        totalCount = totalCount + 1

        scriptStatus('<<<<< END ITERATION STATE <<<<<')

    # Increment the group counter every 118 wells.
    else:
        groupCount = groupCount + 1
        wellCount = 0
        scriptStatus('++++++++++++ NEW GROUP ++++++++++++')
        logVariables()

else:
    scriptStatus('!!! GAME OVER !!!')
    quit()

####################################################################
# End Module.
####################################################################