#!/usr/bin/env python

"""
MODFLOW 96 Add Batchfile (Python)
MAB.PY
v.1.0.0
By John Gentle
Updated 2016.07.05

Python script to add a vanilla bathcfile to the case scenario input files for use in MODFLOW 96.
See README for usage instructions.
"""

# Run script from parent dir of case folders.

####################################################################
# Imports.
####################################################################
import os
import shutil


####################################################################
# Variables.
####################################################################
batch_file = 'modflow.bf'
print batch_file

batch_file_path = os.path.abspath(batch_file)
print batch_file_path

# root_dir = '/data/03325/jgentle/encompass/modflow/modflow96/data_src/generated_cases/bsgam/gen_2'
root_dir = os.getcwd()
print root_dir


# for subdir, dirs, files in os.walk(root_dir):
#     for d in dirs:
#         print 'dir: ', d
#         # copy batchfile into directory.
#         shutil.copy(batch_file, current_scenario_destdir)

    # for subd in subdir:
    #     print 'subdir: ', subd

    # for f in files:
    #     print 'file: ', os.path.join(subdir, f)
