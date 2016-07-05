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

root_dir = '/data/03325/jgentle/encompass/modflow/modflow96/data_src/generated_cases/bsgam/gen_2'
# current_dir = os.getcwd()
model_src_dir = root_dir
# model_src_dir = current_dir
# print model_src_dir
model_src_path = os.path.abspath(model_src_dir)
print model_src_path

# for case in model_src_path:
#     case_dir = os.path.abspath(case)
#     print case_dir

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        print 'file: ', os.path.join(subdir, file)
