from __future__ import print_function
import sys
import json
import argparse

# from specparser import parse_specfile
from tests import run_tests
from model_methods import *
from model_2_methods import create_spec_2_model, transform_spec2_to_spec1, Specfile2
from go_spec import create_go_spec_model


go_spec = False


def parse_arguments():
    """processes given arguments and stores requested options"""

    arg_parser = argparse.ArgumentParser() #description="TODO")

    arg_parser.add_argument('-i', '--input', dest="input", type=str,
                            help="path to input specfile")

    arg_parser.add_argument('-t', '--test', dest="test", type=int, choices=[0,1], default=0,
                            help="turns on/off (1/0) tests run")

    arg_parser.add_argument('-j', '--json', dest="json", type=int, choices=[0,1], default=0,
                            help="turns on/off (1/0) output in json")

    arg_parser.add_argument('-s', '--specfile', dest="specfile", type=int, choices=[0,1], default=0,
                            help="turns on/off (1/0) output as a specfile")

    arg_parser.add_argument('-r', '--reduced', dest="reduced", type=int, choices=[0,1], default=1,
                            help="turns on/off (1/0) reduced output in json, outputs only non-empty fields")

    arg_parser.add_argument('-c', '--config', dest="config", type=str,
                            help="path to configuration file")

    arg_parser.add_argument('-p', '--pretty-print', dest="pretty", type=int, choices=[0,1], default=0,
                            help="output specfile in a normalized form")

    arg_parser.add_argument('-m', '--model', dest="model", type=int, choices=[1,2], default=2,
                            help="choose between specfile 1.0 and 2.0 abstract models")

    arg_parser.add_argument('--debug', dest="debug", type=int, choices=[0,1], default=0,
                            help="for testing and debugging purposes")

    return arg_parser.parse_args()



def process_args(args):

    # args.test == 1 => run all available tests
    if args.test:
        run_tests()
        sys.exit(0)

    # args.input is set => read and process input specfile or json file
    if args.input:
        specpath = args.input
    # args.input is not set => get specfile (or json file) location and read and process it
    else:
        specpath = None

    create_abstract_model(specpath)

    # args.specfile is set => read and process input specfile, write output as a specfile 
    if args.specfile:
        class_to_specfile(Specfile, args.pretty)

    # args.model is set to 1 => output json in specfile 1.0 form
    if args.model and args.model == 1:

        # args.config is set => apply changes from given configuration file on specfile
        if args.config:
            process_config_file(Specfile, args.config)

    # args.model is not set or set to 2 => output specfile or json in specfile 2.0 form
    else:
        create_spec_2_model(Specfile)

        # args.config is set => apply changes from given configuration file on specfile
        # if args.config:
        #     process_config_file(Specfile, args.config)

    # args.json is set => read and process input specfile, write output in json
    if args.json:
        if args.model and args.model == 1:
            print_json_representation(Specfile, args.reduced)
        else:
            print_json_representation(Specfile2, args.reduced)

    # args.debug is set => read and process input specfile, transform into 2.0 and then back to 1.0
    if args.debug:
        Specfile1 = transform_spec2_to_spec1(Specfile2)
        print(json.dumps(remove_empty_fields(Specfile1), default=lambda o: o.__dict__, sort_keys=True))

    if go_spec:     # TODO how to determine?
        create_go_spec_model(Specfile2)


def main():
    """MAIN"""

    args = parse_arguments()

    process_args(args)

    return 0



if __name__ == "__main__":
    main()
