####################################################################
# Imports.
####################################################################

# import sys, inspect
import os

# current_dir = os.path.abspath('')
current_dir = os.getcwd()

# Run script from parent dir of case folders.
modelsourcedir = '.'
model_src_dir = modelsourcedir
print model_src_dir
model_src_path = os.path.abspath(model_src_dir)
print model_src_path

for case in model_src_path:
    print case
