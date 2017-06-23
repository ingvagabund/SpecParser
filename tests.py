from __future__ import print_function
import os, sys, subprocess, filecmp, shutil



def run_tests():
    
    tests_descriptions = [  
        "TESTING TRANSFORMATION OF SPECFILE TO SPECFILE CLASS JSON REPRESENTATION",
        "TESTING TRANSFORMATION OF SPECFILE CLASS TO SPECFILE"
        ]

    testing_specfiles = os.listdir(os.curdir + '/Tests/Inputs')
    reference_output_folders = os.listdir(os.curdir + '/Tests/RefOutputs')

    for testing_set in range(len(reference_output_folders)):

        output_filepath = './Tests/Outputs/' + str(testing_set)
        if os.path.exists(output_filepath):
            shutil.rmtree(output_filepath)
        os.makedirs(output_filepath)

        test_number = 1
        failures = 0

        print('\n' + tests_descriptions[testing_set] + '\n')

        for specfile_filename in testing_specfiles:
            
            os.system('python specparser_main.py -i ./Tests/Inputs/' + specfile_filename + ' > ./Tests/Outputs/' + str(testing_set) + '/' + specfile_filename)
            
            intro = 'TEST ' + str(test_number) + ': '

            if filecmp.cmp('./Tests/Outputs/' + str(testing_set) + '/' + specfile_filename, './Tests/RefOutputs/' + str(testing_set) + '/' + specfile_filename):
                sys.stdout.write(intro + "\033[0;32m" + "SUCCESS!\n" + "\033[0;0m")
            else:
                sys.stdout.write(intro + "\033[1;31m" + "FAIL!" + "\033[0;0m" + " (" + specfile_filename + ")\n")
                failures += 1

            test_number += 1

    print('\nAll tests checked, totalling ' + str(failures) + ' errors!')

    return
