from __future__ import print_function
import sys
import argparse

# from specparser import parse_specfile
from tests import run_tests
from model_methods import create_abstract_model


def parse_arguments():
    """processes given arguments and stores requested options"""

    arg_parser = argparse.ArgumentParser() #description="TODO")

    arg_parser.add_argument('-i', '--input', dest="input", type=str,
    help="path to input specfile")

    arg_parser.add_argument('-t', '--test', dest="test", type=int, choices=[0,1], default=0,
                            help="turns on/off (1/0) tests run")

    return arg_parser.parse_args()



def main():
    """MAIN"""

    args = parse_arguments()

    # args.input is set => read and process input specfile
    if args.input:
        create_abstract_model(args.input)

    # args.test == 1 => run all available tests
    elif args.test:
        run_tests()
        sys.exit(0)

    return 0



if __name__ == "__main__":
    main()
