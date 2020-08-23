#!/usr/bin/env python3
import sys
import zipfile
from os import path
from optparse import OptionParser

usage = "usage: %prog [options] zipped_package_location destination_package_location"
parser = OptionParser(usage=usage)
parser.add_option("-d",
                    help="Extract project into existing directory.",
                    action="store_true",
                    dest="directory",
                    default=False)

(options, args) = parser.parse_args()

print("option parser", options.directory)
print("option parser args", args)

home_directory = path.dirname(path.realpath(__file__))

if len(args) > 1:
    final_project_path = home_directory+"/"+args[1]
    zipped_project_path = home_directory+"/"+args[0]

else:
    print("Error: 2 arguments required {} provided".format(len(sys.argv)-1))
    exit()

if not path.exists(zipped_project_path):
    print("Error: Zipped Project doesn't exist")
    exit()

ext = zipped_project_path.split('.')[-1]

if (ext != "zip" ) and (ext != "gz"):
    print("Error: Unknown project file format. Must be zip or gz")
    exit()

if options.directory:
    if not path.exists(final_project_path):
        print("Error: Destination directory does not exist.")
        exit()

print("Hello all")