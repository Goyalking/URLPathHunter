#!/usr/bin/env python3

import os
import subprocess
import argparse


dirsearch_cmd = 'dirsearch'


default_extensions = 'xml,json,sql,db,log,yml,yaml,bak,txt,tar.gz'


default_excluded_codes = '301,403,404,502,503,400,500'


target_website = 'https://www.tripadvisor.com/'
wordlist_file = '/home/username/Documents/SecLists/Discovery/Web-Content/combined_directories.txt'  # Update this path


parser = argparse.ArgumentParser(description='Dirsearch automation script')
parser.add_argument('-t', '--target', help='Target website URL')
parser.add_argument('-w', '--wordlist', help='Custom wordlist file path')
parser.add_argument('-e', '--extensions', help='Comma-separated list of extensions to search for')
parser.add_argument('-x', '--excluded-codes', help='Comma-separated list of excluded status codes')
args = parser.parse_args()


if args.target:
    target_website = args.target
if args.wordlist:
    wordlist_file = args.wordlist
if args.extensions:
    default_extensions = args.extensions
if args.excluded_codes:
    default_excluded_codes = args.excluded_codes


if not os.path.exists(wordlist_file):
    print(f"Error: Wordlist file '{wordlist_file}' not found.")
    exit(1)


cmd = [
    "dirsearch", 
    "-e", default_extensions,
    "-x", default_excluded_codes,
    "-u", target_website,
    "-w", wordlist_file
]


print(f'Running dirsearch command: {" ".join(cmd)}')
result = subprocess.run(cmd, shell=False)

if result.returncode == 0:
    print('Dirsearch completed successfully.')
else:
    print(f'Dirsearch encountered an error. Return code: {result.returncode}')
