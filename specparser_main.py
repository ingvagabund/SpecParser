from __future__ import print_function
import sys, json
import argparse

# from specparser import parse_specfile
from tests import run_tests
from model_methods import *


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

    # args.config is set => apply changes from given configuration file on specfile
    if args.config:
        process_config_file(Specfile, args.config)

    # args.json is set => read and process input specfile, write output in json 
    if args.json:
        if args.reduced:
            print(json.dumps(remove_empty_fields(Specfile), default=lambda o: o.__dict__, sort_keys=True))
        else:
            print(json.dumps(Specfile, default=lambda o: o.__dict__, sort_keys=True))

    # args.specfile is set => read and process input specfile, write output as a specfile 
    if args.specfile:
        class_to_specfile(Specfile, args.pretty)



def main():
    """MAIN"""

    args = parse_arguments()

    process_args(args)

    return 0



if __name__ == "__main__":
    main()
