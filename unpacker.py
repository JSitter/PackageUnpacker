#!/usr/bin/env python3
import sys
import zipfile
import os

home_directory = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) > 1:
    project_directory = sys.argv[1]
    project_path = home_directory+"/"+sys.argv[1]

else:
    print("ERROR: Project Directory Not Specified")
    exit()

print("project directory", project_directory)
