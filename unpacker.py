#!/usr/bin/env python3
import sys
import zipfile
import gzip
from os import path
from optparse import OptionParser

def unpack_zip(source, destination):
    zipReference = zipfile.ZipFile(source, 'r')
    zipReference.extractall(destination)
    zipReference.close()

def unpack_gz(source, destination):
    print("Unpack gz")

def unpack_zip_into(source, destination):
    print("Unpack into")

def unpack_gz_into(source, destination):
    print("Unpack gz into")

if __name__ == "__main__":
    usage = "usage: %prog [options] zipped_package_location destination_package_location"
    parser = OptionParser(usage=usage)
    parser.add_option("-d",
                        help="Extract project into existing directory.",
                        action="store_true",
                        dest="directory",
                        default=False)

    (options, args) = parser.parse_args()
    home_directory = path.dirname(path.realpath(__file__))

    if len(args) > 1:
        final_project_path = home_directory+"/"+args[1]
        zipped_project_path = home_directory+"/"+args[0]
    else:
        raise Exception("Error: 2 arguments required {} provided".format(len(sys.argv)-1))

    if not path.exists(zipped_project_path):
        raise Exception("Error: Zipped Project doesn't exist")

    # May not be needed -- should rely on errors thrown by zipping package
    ext = zipped_project_path.split('.')[-1]
    if (ext != "zip" ) and (ext != "gz"):
        raise Exception("Error: Unknown project file format. Must be zip or gz")
    if options.directory:
        if not path.exists(final_project_path):
            raise Exception("Error: Destination directory does not exist.")

    if options.directory:
        if ext == "zip":
            unpack_zip_into(zipped_project_path, final_project_path)
        else:
            unpack_gz_into(zipped_project_path, final_project_path)
    else:
        if ext == "zip":
            unpack_zip(zipped_project_path, final_project_path)
        else:
            unpack_gz(zipped_project_path, final_project_path)
