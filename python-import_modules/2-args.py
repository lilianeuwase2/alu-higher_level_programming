#!/usr/bin/python3
import sys

args = sys.argv[1:]
count =i len(args)

if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print("{} arguments:".format(count))

for i, arg in enumerate(args, 1):
    print("{}: {}".format(i, arg))
