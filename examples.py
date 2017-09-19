from __future__ import print_function
import os
import shutil



def run_examples():

    source_filepath = './Examples/Inputs/'
    example_specfiles = os.listdir(os.curdir + source_filepath[1:])
    output_filepath = './Examples/Outputs/'

    if os.path.exists(output_filepath):
        shutil.rmtree(output_filepath)
    os.makedirs(output_filepath)

    for example_filename in example_specfiles:
        os.system('python specparser_main.py -m 3 -j 1 -g 1 -i ' + source_filepath + example_filename + ' > ./Examples/Outputs/' + example_filename)

    return
