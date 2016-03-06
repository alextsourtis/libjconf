#!/usr/bin/env python3

import argparse     # https://docs.python.org/3/library/argparse.html
import configparser # https://docs.python.org/3/library/configparser.html
import re

###############################################################################
# arguments
###############################################################################
parser = argparse.ArgumentParser(description='Configuration made for humans')

parser.add_argument('-p', '--parse', required=True, dest='config_file',
                    help='Parse a configuration file to a human readable one')

args = parser.parse_args()

print('Config file given:', args.config_file)

###############################################################################
# config parser checks
###############################################################################
config = configparser.ConfigParser()
config.read(args.config_file)
print('Sections:', config.sections())

for section in config.sections():
    print('Section:', section)

    for key in config[section]:
        print('\t',key)

DEFAULT = 'DEFAULT'

if DEFAULT in config:
    print('Section:', DEFAULT)
    for key in config[DEFAULT]:
        print('\t',key)

###############################################################################
# implementation
###############################################################################
section = re.compile('^\[(?P<section>[a-zA-Z0-9-_.]+)\]$')
key = re.compile('^(?P<key>[a-zA-Z0-9-_.]+)[ ]*=[ ]*(?P<value>[a-zA-Z0-9-_.]*)$')

parsed_config_dict = {}
current_section = None

with open(args.config_file, 'r') as config_file:
    for line in config_file.readlines():
        line = line.strip()
        
        match_section = section.match(line)
        if match_section:
            # print(match_section.group('section'))
            current_section = match_section.group('section')
            parsed_config_dict[current_section] = {}
            
        match_key = key.match(line)
        if match_key:
            # print('\t %s %s' % (match_key.group('key'), match_key.group('value')))
            if current_section:
                parsed_config_dict[current_section][match_key.group('key')] = match_key.group('value')
            
print(parsed_config_dict)
    







