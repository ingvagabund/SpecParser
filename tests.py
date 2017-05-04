from __future__ import print_function
import os, sys, subprocess, filecmp


testing_specfiles = os.listdir(os.curdir + '/Tests/Inputs')
number = 1
failures = 0

for specfile_filename in testing_specfiles:
    os.system('python abstract_model.py -i ./Tests/Inputs/' + specfile_filename + ' > ./Tests/Outputs/' + specfile_filename)
    
    intro = 'TEST ' + str(number) + ': '

    if filecmp.cmp('./Tests/Outputs/' + specfile_filename, './Tests/RefOutputs/' + specfile_filename):
        sys.stdout.write(intro + "\033[0;32m" + "SUCCESS!\n" + "\033[0;0m")
        number = number
    else:
        sys.stdout.write(intro + "\033[1;31m" + "FAIL!" + "\033[0;0m" + " (" + specfile_filename + ")\n")
        failures += 1

    number += 1

print('All tests checked, totalling ' + str(failures) + ' errors!')
