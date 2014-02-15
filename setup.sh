#!/bin/bash

cwd="$(pwd)"
en_path="$cwd/encrypt_me.py"
de_path="$cwd/decrypt_me.py"
chmod 555 $en_path
chmod 555 $de_path
cp $en_path /bin/encrypt_me
cp $de_path /bin/decrypt_me
echo "Installed successfully. Try to use encrypt_me and decrypt_me"
