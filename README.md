# assess_dope
Assess models previously generated with Modeller with the DOPE method

## Usage
```
assess_dope [-h] [-o OUTPUT] [-v] model [model ...]

positional arguments:
  model                 Structural model previously generated with Modeller.

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        CSV output file containing the DOPE assessment values per each input model [default:
                        dope_assessment.csv].
  -v, --version         Show program's version number and exit  
```
## Installation
This is a Python script, so, you can just run the assess_dope.py file or put a symbolic link in any directory of your PATH (e.g. /usr/local/bin).

## Dependencies
* Python3
* argparse
* [Modeller](https://salilab.org/modeller/)

## OSs
Tested on Linux.
