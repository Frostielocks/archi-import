# archi-import
```
usage: archi-import [-h] [-o OUTPUT] [-s SPECIALIZATION] [-v] type input

Create an archi import csv file given a list of names

positional arguments:
  type                  type of ArchiMate elements to be imported
  input                 path to the input file containing the list of names

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to the output file (or directory), default is
                        "elements.csv"
  -s SPECIALIZATION, --specialization SPECIALIZATION
                        specialization for the ArchiMate elements
  -v, --verbose         show verbose output

See also https://github.com/Frostielocks/archi-import
```