#!/usr/bin/env python

import os
import shutil

wells_src_dir = 'well_scalars'
wells_src_path = os.path.abspath(wells_src_dir)
wells_dest_dir = 'parameterized_well_scalars'
wells_dest_path = os.path.abspath(wells_dest_dir)

print ' '
print '>>> START GAME <<<'
print ' '
# print 'wells_src_dir: ', wells_src_dir
print 'wells_src_path: ', wells_src_path
# print 'wells_dest_dir: ', wells_dest_dir
print 'wells_dest_path: ', wells_dest_path

well_src_files = os.listdir(wells_src_path)
print ('well_src_files %s' % well_src_files)
# print ' '

for well_src in well_src_files:

    groupCount = 0
    wellCount = 0

    while (groupCount < 81):

        # Build directory name for case.
        current_group_dir = 'well_scalars_' + str(groupCount)
        current_group_dir_path = wells_dest_path + '/' + current_group_dir

        # Create directory if it does not exist.
        if not os.path.exists(current_group_dir_path):
            os.makedirs(current_group_dir_path)

        if (wellCount < 119):
            print '----------------------------------------------------------------------------'
            current_well_file = wells_src_path + '/' + well_src
            print ('The current_well_file is: %s' % current_well_file)
            # print ('The current well_src is: %s' % well_src)
            print ('The current_group_dir_path is: %s' % current_group_dir_path)

            if (os.path.isfile(current_well_file)):
                shutil.copy(current_well_file, current_group_dir_path)
            print ('The wellCount is: %s' % wellCount)
            wellCount = wellCount + 1
            # quit()
        else:
            groupCount = groupCount + 1
            wellCount = 0
            print '++++++++++++++++++++++++++++++++++++++++++'
            print ('The groupCount is: %s' % groupCount)
            print ('The wellCount is: %s' % wellCount)
            # quit()

else:
    print '!!! GAME OVER !!!'
    quit()
