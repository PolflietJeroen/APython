#!/usr/bin/encv python
import argparse
import os.path
from argparse import ArgumentParser


def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return open(arg, 'r')
def is_valid_file_make_it(parser, arg):
#    if not os.path.exists(arg):
#       parser.error("The file %s does not exist!" % arg)
#   else:
        return open(arg, 'w')
    
parser = ArgumentParser(description="2 inputfiles and one outputfile")
parser.add_argument("-i1", dest="input1", required=True,
        help="2 inputfiles and one outputfile", metavar="FILE",
        type=lambda x: is_valid_file(parser, x))
parser.add_argument("-i2", dest="input2", required=True,
        help="2 inputfiles and one outputfile", metavar="FILE",
        type=lambda x: is_valid_file(parser, x))
parser.add_argument("-o", dest="output", required=True,
        help="2 inputfiles and one outputfile", metavar="FILE",
        type=lambda x: is_valid_file_make_it(parser, x))
args = parser.parse_args()

#for line in args.input1:
#    print (line)

in1 = set(line.strip() for line in args.input1)
in2 = set(line.strip() for line in args.input2)
in3 = in1 | in2
print in1
print in2
print in3

for item in in3:
  args.output.write("%s\n" % item)
