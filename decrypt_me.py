#!/usr/local/bin/python

import sys
import getpass
import commands
from simplecrypt import encrypt, decrypt

pwd = getpass.getpass('Enter Password: ')
if len(sys.argv) < 2:
    in_name = raw_input('Enter input file name: ')
else:
    in_name = sys.argv[1]

in_file = open(in_name, 'r')
txt = decrypt(pwd, in_file.read())
print txt
