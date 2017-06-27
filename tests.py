from __future__ import print_function
import os, sys, subprocess, filecmp, shutil



def run_tests():
    
    tests_descriptions = [  
        "TESTING TRANSFORMATION OF SPECFILE TO SPECFILE CLASS JSON REPRESENTATION",
        "TESTING TRANSFORMATION OF SPECFILE CLASS TO SPECFILE",
        "TESTING TRANSFORMATION OF JSON INPUT TO SPECFILE"
    ]

    arguments = [
        '-j 1 -s 0',
        '-j 0 -s 1',
        '-j 0 -s 1'
    ]

    testing_specfiles = os.listdir(os.curdir + '/Tests/Inputs')
    reference_output_folders = os.listdir(os.curdir + '/Tests/RefOutputs')
    failures = 0    

    for testing_set in range(len(reference_output_folders)):

        output_filepath = './Tests/Outputs/' + str(testing_set)
        if os.path.exists(output_filepath):
            shutil.rmtree(output_filepath)
        os.makedirs(output_filepath)

        test_number = 1

        print('\n' + tests_descriptions[testing_set] + '\n')

        for specfile_filename in testing_specfiles:
            
            if testing_set == 2:
                source_file_path = ' -i ./Tests/RefOutputs/0/'
            else:
                source_file_path = ' -i ./Tests/Inputs/'

            os.system('python specparser_main.py ' + arguments[testing_set] + source_file_path + specfile_filename + ' > ./Tests/Outputs/' + str(testing_set) + '/' + specfile_filename)
            
            intro = 'TEST ' + str(test_number) + ': '

            if testing_set > 0:
                reference_output_path = './Tests/Inputs/' + specfile_filename
            else:
                reference_output_path = './Tests/RefOutputs/' + str(testing_set) + '/' + specfile_filename

            if filecmp.cmp('./Tests/Outputs/' + str(testing_set) + '/' + specfile_filename, reference_output_path, False):
                sys.stdout.write(intro + "\033[0;32m" + "SUCCESS!\n" + "\033[0;0m")
            else:
                sys.stdout.write(intro + "\033[1;31m" + "FAIL!" + "\033[0;0m" + " (" + specfile_filename + ")\n")
                failures += 1

            test_number += 1

    print('\nAll tests checked, totalling ' + str(failures) + ' errors!')

    return
