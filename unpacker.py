#!/usr/bin/env python3
import sys
import zipfile
import os

if len(sys.argv) > 1:
    project_directory = sys.argv[1]
    project_path = home_directory+"/"+sys.argv[1]

else:
    print("ERROR: Project Directory Not Specified")
    exit()

print("project directory", project_directory)
