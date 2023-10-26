#!/usr/bin/env python3
## Assess models previously generated with modeller with the DOPE method.
##
## Amaury Pupo Merino
## amaury.pupo@gmail.com
##
## This script is released under GPL v3.
##

## Importing modules
import argparse
import sys
from modeller import *
from modeller.scripts import complete_pdb

## Functions
def assess_dope(filename):
    """Assess a whole model with the DOPE method
    """
    env = Environ()
    env.libs.topology.read(file='$(LIB)/top_heav.lib')
    env.libs.parameters.read(file='$(LIB)/par.lib')

    mdl = complete_pdb(env, filename)

    # Select all atoms in the model
    atmsel = Selection(mdl)

    return atmsel.assess_dope()

def write_output(dope_assessments, filename):
     """Write CSV output file containing the DOPE assessment values per each input model
     """
    
     with open(filename, "w") as output_file:
         output_file.write("model,DOPE\n")
         for model,dope in dope_assessments.items():
             output_file.write("{},{:f}\n".format(model,dope))      

## Main
def main():
    """Main function.
    """
    parser=argparse.ArgumentParser(description="Assess models previously generated with Modeller with the DOPE method.")
    parser.add_argument('model', nargs='+', help='Structural model previously generated with Modeller.')
    parser.add_argument('-o', '--output', default='dope_assessment.csv', help='CSV output file containing the DOPE assessment values per each input model [default: %(default)s].')
    parser.add_argument('-v', '--version', action='version', version='1.1', help="Show program's version number and exit.")

    args=parser.parse_args()

    dope_assessments = {}

    for m in args.model:
        dope_assessments[m] = assess_dope(m)

    if dope_assessments:
        write_output(dope_assessments,args.output)

## Running the script
if __name__ == "__main__":
        main()
