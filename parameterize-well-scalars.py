#!/usr/bin/env python

import os
import shutil

wells_src_dir = 'well_scalars'
wells_src_path = os.path.abspath(wells_src_dir)
wells_dest_dir = 'parameterized_well_scalars'
wells_dest_path = os.path.abspath(wells_dest_dir)


for well in wells_src_path:
    groupCount = 0
    wellCount = 0

    while (groupCount < 81):

        # Build directory name for case.
        current_group_dir = wells_dest_path + '/well_scalars_' + str(groupCount)

        print ('The current group directory is %s' % current_group_dir)

        # Create directory if it does not exist.
        if not os.path.exists(current_group_dir):
            os.makedirs(current_group_dir)

        if (wellCount < 119):
            print ('The current well file is %s' % well)
            shutil.copy(well, current_group_dir)
            print ('The wellCount is %s' % wellCount)
            wellCount = wellCount + 1
        else:
            groupCount = groupCount + 1
            wellCount = 0
            print ('The groupCount is now %s' % groupCount)
            print ('The wellCount is now %s' % wellCount)

    else:
        quit()
