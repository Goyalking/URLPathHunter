#!/usr/bin/env python3

import os
import subprocess
import argparse

# Define the dirsearch command
dirsearch_cmd = 'dirsearch'

# Define the default extensions to search for
default_extensions = 'xml,json,sql,db,log,yml,yaml,bak,txt,tar.gz'

# Define the default excluded status codes
default_excluded_codes = '301,403,404,502,503,400,500'

# Define the target website and wordlist file paths
target_website = 'https://www.example.com/'
wordlist_file = '/home/username/Documents/wordlist.txt'  # Update this path

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Dirsearch automation script')
parser.add_argument('-t', '--target', help='Target website URL')
parser.add_argument('-w', '--wordlist', help='Custom wordlist file path')
parser.add_argument('-e', '--extensions', help='Comma-separated list of extensions to search for')
parser.add_argument('-x', '--excluded-codes', help='Comma-separated list of excluded status codes')
args = parser.parse_args()

# Update target website, wordlist file path, extensions, and excluded codes if provided
if args.target:
    target_website = args.target
if args.wordlist:
    wordlist_file = args.wordlist
if args.extensions:
    default_extensions = args.extensions
if args.excluded_codes:
    default_excluded_codes = args.excluded_codes

# Check if wordlist file exists
if not os.path.exists(wordlist_file):
    print(f"Error: Wordlist file '{wordlist_file}' not found.")
    exit(1)

# Construct the dirsearch command with the provided arguments
cmd = [
    "dirsearch",  # Ensure dirsearch is installed and accessible in PATH
    "-e", default_extensions,
    "-x", default_excluded_codes,
    "-u", target_website,
    "-w", wordlist_file
]

# Run the dirsearch command
print(f'Running dirsearch command: {" ".join(cmd)}')
result = subprocess.run(cmd, shell=False)

if result.returncode == 0:
    print('Dirsearch completed successfully.')
else:
    print(f'Dirsearch encountered an error. Return code: {result.returncode}')
