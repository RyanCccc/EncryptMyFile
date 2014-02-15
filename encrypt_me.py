import sys
import getpass
import commands
from simplecrypt import encrypt, decrypt

pwd = getpass.getpass('Enter Password:')
pwd2 = getpass.getpass('Reenter Password:')
if not pwd == pwd2:
    print 'Passwords not same'
    exit(0)
if len(sys.argv) < 2:
    in_name = raw_input('Enter input file name: ')
    out_name = raw_input('Enter output file name: ')
else:
    in_name = sys.argv[1]
    out_name = sys.argv[2]

in_file = open(in_name, 'r')
out_file = open(out_name, 'w')
txt = encrypt(pwd, in_file.read())
out_file.write(txt)
out_file.flush()
print 'Encrypted successfully. Encrypted file name:', out_name
should_rm = raw_input('Do you want to remove '+in_name+'? y/n: ')
if should_rm == 'y':
   commands.getoutput('rm '+in_name)
   print 'Successfully removed', in_name
