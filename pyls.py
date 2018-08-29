#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("target")
parser.add_argument("-l", "--limit", type=int, default=0, help="Only print the given number of files")
parser.add_argument("-r", "--recursive", action="store_true", help="Print contents of subdirectories as well")
parser.add_argument("-v", "--verbose", action="store_true", help="Print file sizes along with file names")

parser.parse_args()

print("This is only a test")
