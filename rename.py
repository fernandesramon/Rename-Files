#!/usr/bin/python3

"""Renames the files in the given directories a naming convention.

Only renames regular files (i.e. it ignores subdirectories and hidden files). 
The naming convention is: DIR_NAME - # of COUNT
where DIR_NAME is the directory name, COUNT is the total number of files in the
directory, and # is an incrememnting int for each file. The files are ordered
by date modified (i.e. the oldest file is #1).
"""

import os
import sys
from time import sleep
from stat import ST_CTIME

def usage():
    """Prints usage message to console
    """
    print("Usage:")
    print("     python3 rename.py path [paths]")

def exit_with_error(msg=None):
    """Exits with error, printing the given message
    """
    if msg is not None:
        print(msg)
    usage()
    sys.exit(1)

def main():
    """Main runner
    """
    if len(sys.argv)  == 1:
        exit_with_error("1 or more directories must be specified")

    dirs = [dir for dir in sys.argv[1:] if os.path.isdir(dir)]
    for dir in dirs:
        foldername = os.path.basename(dir)
        print("Processing {}...".format(foldername))
        files = [dir + "/" + f.name for f in os.scandir(dir) if 
            os.path.isfile(f.path) and not f.name.startswith('.')]
        count = len(files)
        files.sort(key=os.path.getmtime)
        os.mkdir(dir + "/" + "tmp_rename")

        for i, oldname in enumerate(files):
            ext = os.path.splitext(oldname)[1]
            newname = dir + "/tmp_rename/{} - {} of {}{}".format(foldername, i+1, count, ext)
            os.rename(oldname, newname)
        sleep(0.5)

        for i, oldname in enumerate(files):
            ext = os.path.splitext(oldname)[1]
            oldname = dir + "/tmp_rename/{} - {} of {}{}".format(foldername, i+1, count, ext)
            newname = dir + "/{} - {} of {}{}".format(foldername, i+1, count, ext)
            os.rename(oldname, newname)
        os.rmdir(dir + "/" + "tmp_rename")
        print("DONE")

if __name__ == "__main__":
    main()
