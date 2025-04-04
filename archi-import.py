import argparse

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
    if verbose:
        print("Reading names from {0}...".format(filename))

    names = []
    # TODO do any sanitization?
    with open(filename, 'r') as fd:
        names = fd.readlines()
    
    if verbose and names:
        print("Read {0} names successfully!".format(len(names)))
    return names


def write_csv_to_file(csv_string, filename, verbose=False):
    if verbose:
        print("Writing csv to {0}...".format(filename))
    
    bytes_written = 0
    with open(filename, 'w+') as fd:
        bytes_written = fd.write(csv_string)

    if verbose:
        print("Wrote {0} bytes to {1}!".format(bytes_written, filename))
    return bytes_written

def initialize_parser():
    """
    Initialize a new parser object.

    Returns:
        ArgumentParser: an initialized parser object
    """
    parser = argparse.ArgumentParser(
        prog='archi-import - Import a list as archi elements',
        description='Creates a elements.csv file to be used by archi to populate elements.',
        epilog='For more information, contact the AppSec team.'
    )

    parser.add_argument('type', 
        help="the type of the specified elements")
    parser.add_argument('input',
        help="the input file containing a list of element names")
    parser.add_argument('-o', '--output', default="elements.csv",
        help="")
    parser.add_argument('-s', '--specialization',
        help="") 
    parser.add_argument('-v', '--verbose', action='store_true', 
        help="show verbose output")

    return parser


def main():
    """The entrypoint for this script."""
    parser = initialize_parser()
    args = parser.parse_args()

    if args.verbose:
        print("Starting...")
    
    names = read_names_from_file(filename=args.input, verbose=args.verbose)
    csv_string = convert_names_to_csv(names=names, type=args.type, specialization=args.specialization, verbose=args.verbose)
    write_csv_to_file(csv_string=csv_string, filename=args.output, verbose=args.verbose)

    if args.verbose:
        print("Finished!")

main()