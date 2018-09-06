#!/usr/bin/python3

import argparse
from pathlib import Path

class LS:
    def __init__(self, verbose, limit, recursive):
        self.verbose = verbose
        self.limit = limit
        self.recursive = recursive

    def ls_print(self, path):
        # Print path, and size if verbose
        if self.verbose:
            print("%08d %s" % (path.stat().st_size, str(path)))
        else:
            print(str(path))

    def ls(self, path, count):
        # If limit reached, bail out
        if count > 0 and count == self.limit:
            return count
        # Print current path
        self.ls_print(path)
        count = count + 1
        # Handle directory, and any subdirectories if recursive
        if not path.is_file() and (count == 1 or self.recursive):
            for target in path.iterdir():
                count = self.ls(target, count)
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
    app = LS(args.verbose, args.limit, args.recursive)
    path = Path(args.target)
    app.ls(path, 0)

if __name__ == "__main__":
    main()
