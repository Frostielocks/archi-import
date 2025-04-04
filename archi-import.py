import argparse
import os

def convert_names_to_csv(names, type, specialization="", verbose=False):
    """

    Parameters:
        names: the input list of names

    Returns:
        String: the output csv string
    """
    if verbose:
        print("Converting names to csv...")

    preamble = '"ID","Type","Name","Documentation","Specialization"\n'
    string_builder = preamble
    for name in names:
        string_builder += '"","' + type +'","' + name + '","","' + specialization + '"\n'
    
    if verbose and not string_builder == preamble:
        print("Converted names to csv successfully!")
    return string_builder


def read_names_from_file(filename, verbose=False):
    """
    """
    if verbose:
        print("Reading names from {0}...".format(filename))

    names = []
    # TODO do any sanitization?
    with open(filename, 'r') as fd:
        names = fd.readlines()
    
    if verbose:
        if names:
            print("Read {0} names successfully!".format(len(names)))
        else:
            print("Found no names.")
    return names


def write_csv_to_file(csv_string, filename, verbose=False):
    """
    """
    if verbose:
        print("Writing csv to {0}...".format(filename))
    
    bytes_written = 0
    with open(filename, 'w+') as fd:
        bytes_written = fd.write(csv_string)

    if verbose:
        print("Wrote {0} bytes to {1}!".format(bytes_written, filename))
    return bytes_written


def sanitize_output(output_path, verbose=False):
    """
    """
    if os.path.exists(output_path) and os.path.isdir(output_path):
        new_output_path = output_path + ('' if output_path.endswith('/') else '/') + 'elements.csv'
        
        if verbose:
            print("Adjusted output path to {0}".format(new_output_path))
        
        return new_output_path
    
    elif output_path.endswith("/elements.csv") or output_path == "elements.csv":
        return output_path
    
    else:
        raise ValueError("output filename should either be an existing directory or end with \"elements.csv\"")


def initialize_parser():
    """
    Initialize a new parser object.

    Returns:
        ArgumentParser: an initialized parser object
    """
    parser = argparse.ArgumentParser(
        prog='archi-import',
        description='Create an archi import csv file given a list of names',
        epilog='See also https://github.com/Frostielocks/archi-import'
    )

    parser.add_argument('type', 
        help="type of ArchiMate elements to be imported")
    parser.add_argument('input',
        help="path to the input file containing the list")

    parser.add_argument('-o', '--output', default="elements.csv",
        help="path to the output file (or directory), default is \"elements.csv\"")
    parser.add_argument('-s', '--specialization',
        help="specialization for the ArchiMate elements") 
    parser.add_argument('-v', '--verbose', action='store_true', 
        help="show verbose output")

    return parser


def main():
    """The entrypoint for this script."""
    parser = initialize_parser()
    args = parser.parse_args()
    args.output = sanitize_output(output_path=args.output, verbose=args.verbose)

    if args.verbose:
        print("Starting...")
    
    names = read_names_from_file(filename=args.input, verbose=args.verbose)
    csv_string = convert_names_to_csv(names=names, type=args.type, specialization=args.specialization, verbose=args.verbose)
    write_csv_to_file(csv_string=csv_string, filename=args.output, verbose=args.verbose)

    if args.verbose:
        print("Finished!")


main()
