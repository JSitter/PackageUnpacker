# Package Unpacker
Shell script that allows for the unpackaging of a zipped project into the directory of your choice. Built using Python 3.5 and Hostgator's shared server in mind.

## Usage
Run `unpacker.py [options] <zipped package location> <final location>`. 
On Hostgator run  `hostgator-runner.sh [options] <zipped package location> <final location>`. 

## Flags
`-d` to unzip project into existing directory instead of creating a new directory.
`-h --help` show help screen.
`-r --replace` replace existing files.