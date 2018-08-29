#!/usr/bin/python3

import argparse
from os import listdir
from os.path import isfile, join, getsize

def ls(path, count, args):
    if count == args.limit:
        return count
    if isfile(path):
        if args.verbose:
            print("%08d %s" % (getsize(path), path))
        else:
            print(path)
        count = count + 1
    else:
        for target in listdir(path):
            if args.recursive:
                count = ls(join(path,target), count, args)
            else:
                print(join(path,target))
                count = count + 1
    return count

parser = argparse.ArgumentParser()

parser.add_argument("target")
parser.add_argument("-l", "--limit", type=int, default=0, help="Only print the given number of files")
parser.add_argument("-r", "--recursive", action="store_true", help="Print contents of subdirectories as well")
parser.add_argument("-v", "--verbose", action="store_true", help="Print file sizes along with file names")

args = parser.parse_args()

ls(args.target, 1, args)
