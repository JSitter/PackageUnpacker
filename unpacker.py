#!/usr/bin/env python3
import zipfile
import tarfile
import os
import shutil
from os import path
from optparse import OptionParser

temp_dir = './.tempdir'


def check_temp_dir():
    if not path.exists(temp_dir):
        os.mkdir(temp_dir)

def unpack_zip(source, destination):
    zipReference = zipfile.ZipFile(source, 'r')
    zipReference.extractall(destination)
    zipReference.close()
    print("Done")

def unpack_gz(source, destination):
    tarball = tarfile.open(source, 'r:gz')
    tarball.extractall(path=destination)
    print("Done")

def unpack_zip_into(source, destination, replace=False):
    zipReference = zipfile.ZipFile(source, 'r')
    allfiles = zipReference.namelist()
    temp_source_dir = "{}/{}".format(temp_dir, allfiles[0])
    check_temp_dir()
    
    zipReference = zipfile.ZipFile(source, 'r')
    zipReference.extractall(temp_dir)
    files = os.listdir(temp_source_dir)

    for file in files:
        file_destination = "{}/{}".format(destination, file)
        if not path.exists(file_destination):
            shutil.move("{}/{}".format(temp_source_dir, file), destination)
        elif replace:
            replace_item("{}/{}".format(temp_source_dir, file), "{}/{}".format(destination, file))
            print("Replaced {}.".format(file))
        else:
            print("Skipping {}. Already Exists. ".format(file))
    shutil.rmtree(temp_source_dir)
    
    zipReference.close()
    print("Done")

def replace_item(source, destination):
    if path.isdir(destination):
        remove_directory(destination)
    else:
        remove_file(destination)
    shutil.move(source, destination)


def unpack_gz_into(source, destination, replace=False):
    tar = tarfile.open(source, 'r:gz')
    allfiles = tar.getnames()
    temp_source_dir = "{}/{}".format(temp_dir, allfiles[0])

    if not path.exists(temp_dir):
        os.mkdir(temp_dir)
    
    tarball = tarfile.open(source, 'r:gz')
    tarball.extractall(path=temp_dir)
    files = os.listdir(temp_source_dir)

    for file in files:
        file_destination = "{}/{}".format(destination, file)
        if not path.exists(file_destination):
            shutil.move("{}/{}".format(temp_source_dir, file), destination)
        elif replace:
            replace_item("{}/{}".format(temp_source_dir, file), "{}/{}".format(destination, file))
            print("Replaced {}.".format(file))
        else:
            print("Skipping {}. Already exists.".format(file))
    shutil.rmtree(temp_source_dir)
    print("Done")

def remove_file(source):
    print("remove file: {}".format(source))
    os.remove(source)

def remove_directory(source):
    print("Remove directory {}".format(source))
    shutil.rmtree(source)
    

if __name__ == "__main__":
    usage = "usage: %prog [options] zipped_package_location destination_package_location"
    parser = OptionParser(usage=usage)
    parser.add_option("-d",
                        help="Extract project into existing directory.",
                        action="store_true",
                        dest="directory",
                        default=False)

    parser.add_option("-r","--replace",
                    help="Replace existing files.",
                    action="store_true",
                    dest="replace",
                    default=False)

    (options, args) = parser.parse_args()
    home_directory = path.dirname(path.realpath(__file__))

    if len(args) > 1:
        final_project_path = home_directory+"/"+args[1]
        zipped_project_path = home_directory+"/"+args[0]
    else:
        raise Exception("Error: 2 arguments required {} provided".format(len(args)-1))

    if not path.exists(zipped_project_path):
        raise Exception("Error: Zipped Project doesn't exist")

    # Needs more robust test of compressed package
    ext = zipped_project_path.split('.')[-1]
    if (ext != "zip" ) and (ext != "gz"):
        raise Exception("Error: Unknown project file format. Must be zip or gz")
    if options.directory:
        if not path.exists(final_project_path):
            raise Exception("Error: Destination directory does not exist.")

    if options.directory:
        if ext == "zip":
            unpack_zip_into(zipped_project_path, final_project_path, options.replace)
        else:
            unpack_gz_into(zipped_project_path, final_project_path, options.replace)
    else:
        if ext == "zip":
            unpack_zip(zipped_project_path, final_project_path)
        else:
            unpack_gz(zipped_project_path, final_project_path)
