#!/usr/bin/python3

import argparse
from os import listdir
from os.path import isfile, join, getsize

def ls_print(path, args):
    # Print path, and size if verbose
    if args.verbose:
        print("%08d %s" % (getsize(path), path))
    else:
        print(path)

def ls(path, count, args):
    # If limit reached, bail out
    if count > 0 and count == args.limit:
        return count
    # Print current path
    ls_print(path, args)
    count = count + 1
    # Handle directory, and any subdirectories if recursive
    if not isfile(path) and (count == 1 or args.recursive):
        for target in listdir(path):
            count = ls(join(path,target), count, args)
    # Keep track of files print
    return count

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("target")
    parser.add_argument("-l", "--limit", type=int, default=0, choices=range(1,10000), metavar="[1-10000]", help="Only print the given number of files")
    parser.add_argument("-r", "--recursive", action="store_true", help="Print contents of subdirectories as well")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print file sizes along with file names")
    args = parser.parse_args()
    # Pass arguments to recursive ls call
    ls(args.target, 0, args)

if __name__ == "__main__":
    main()
