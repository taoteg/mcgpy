#!/usr/bin/env python

"""
MODFLOW 96 Parameterized Well Groups (Python)
MPWG.PY
v.1.0.0
By John Gentle
Updated 2016.07.03

Python script to prepare case scenario input files for use in MODFLOW 96.
See README for usage instructions.
"""

####################################################################
# Imports.
####################################################################
# import os


####################################################################
# Variables.
####################################################################
target_path_A = './inventory.wells_src.sorted.dat'
target_path_B = './inventory.param_wells.trimmed.sorted.dat'
target_iteration_title = ''

# Test file A
# target_file_A = target_path_A
# target_file_B = target_path_A
# target_iteration_title = 'A Test'

# Test file B
# target_file_A = target_path_B
# target_file_B = target_path_B
# target_iteration_title = 'B Test'

# Test A against B
target_file_A = target_path_A
target_file_B = target_path_B
target_iteration_title = 'A > B'

# Test B against A
# target_file_A = target_path_B
# target_file_B = target_path_A
# target_iteration_title = 'B > A'

iterationCountA = 0
iterationCountB = 0
matchCount = 0
missCount = 0
matchList = []
# missList = []


####################################################################
# Methods.
####################################################################
def printIterationState(iterationTitle='tbd'):
    print '----------------------'
    print '<<<<< iteration: ' + iterationTitle + ' >>>>>'
    print '----------------------'
    print 'iterationCountA: ', iterationCountA
    print 'iterationCountB: ', iterationCountB
    print '-------------------'
    print 'matchCount: ', matchCount
    # print '-------------------'
    # print 'matchList: '
    # print matchList
    # print '-------------------'
    print 'missCount: ', missCount
    print '-------------------'
    # print 'missList:'
    # print missList
    print ' '


def compareFiles():
    # fn = os.path.join(os.path.dirname(__file__), 'my_file')
    with open(target_file_A) as file_a:
        # content = file_a.readlines()
        content_A = [line.strip('\n') for line in file_a.readlines()]
        # print content_A
        # return content_A

    # fn = os.path.join(os.path.dirname(__file__), 'my_file')
    with open(target_file_B) as file_b:
        # content = file_b.readlines()
        content_B = [line.strip('\n') for line in file_b.readlines()]
        # print content_B
        # return content_B

        # OUTPUT FOR: content = f.readlines()
        # [
        # ...,
        # 'wells_1a494f6d64bfb2bea49bfea5c6a67183.dat\n',
        # 'wells_1a4ac7a1ce532ac243db9fb5c9f6430e.dat\n',
        # 'wells_1a4c83ee8d842a08220d40b829177304.dat\n'
        # ]

        # OUTPUT FOR: content = [x.strip('\n') for x in f.readlines()]
        # [
        # ...,
        # 'wells_fff1b9e33abae0c51098dc3b5a761d0e.dat',
        # 'wells_fff5b166a8f36ce9b74bfd0bc34849d1.dat',
        # 'wells_fff7ab60896fc668726c0dbd833afa30.dat'
        # ]

    # Iterate over recharge interpretations.
    for line_entry_A in content_A:
        for line_entry_B in content_B:

            if (line_entry_A == line_entry_B):
                matchList.append({line_entry_A, line_entry_B})
                matchCount = matchCount + 1
                # print '+++ MATCHED SRC +++'
                # print 'line_entry_A: ', line_entry_A
                # print 'line_entry_B: ', line_entry_B
                # print 'matchCount: ', matchCount
                # print ' '
                # printIterationState()
            else:
                # missList.append({line_entry_A, line_entry_B})
                missCount = missCount + 1
                # print '!!!!!!!!!!!!!!!!!!!!!'
                # print '!!! UNMATCHED SRC !!!'
                # print line_entry_A
                # print line_entry_B
                # print 'missCount: ', missCount'
                # print '!!!!!!!!!!!!!!!!!!!!!'
                # print ' '
                # printIterationState()

            iterationCountB = iterationCountB + 1
            # printIterationState()

        iterationCountA = iterationCountA + 1
        # printIterationState()

####################################################################
# Start Module.
####################################################################
compareFiles()



printIterationState(target_iteration_title)
####################################################################
# End Module.
####################################################################
