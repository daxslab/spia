# -*- coding: utf-8 -*-

#    SPIA, Simple Python Internationalization API

#    Copyright (C) 2013 Carlos Cesar Caballero Diaz <ccesar@linuxmail.org>
#   
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#from __future__ import print_function
import re
import sys
import os



def _get_internationalized_chains(code_file, function_call = "_"):
    chains = []
    try:
        # open the file
        code_file = open(code_file, "r")           
        # read through the file
        for text in code_file.readlines():
            #strip off the \n
            text = text.rstrip()
            #this is probably not the best way, but it works for now
            regex = re.findall(function_call+'\((["\'])(.*?)(["\'])\)', text)
            # if the regex is not empty and is not already in chains list append
            if regex is not None and regex not in chains and not regex == []:
                chains.append(regex[0][1])
        code_file.close()
    except IOError, (errno, strerror):
        print ("I/O Error(%s) : %s" % (errno, strerror))
        sys.exit(1)

    #remove duplicates
    chains_set = set(chains)
    chains = []
    for chain in chains_set:
        chains.append(chain)

    return chains

def create_chains_file(input_file, output_dir, function_call = "_", lang = "es-cu"):
    chains = _get_internationalized_chains(input_file, function_call)

    if not lang == None:
        file_name = os.path.join(output_dir,lang+".py")
    else:
        file_name = os.path.basename(input_file)
        (name, ext) = os.path.splitext(file_name)
        file_name = os.path.join(output_dir,name+"_SPIA_lang"+ext)

    try:
        file = open(file_name, 'w+')
        file.write('# coding: utf8\n')
        file.write('\n')
        file.write('keys = {\n')
        for chain in chains:
            file.write('\''+chain+'\':\''+chain+'\',\n')
        file.write('}\n')
        file.close()
    except IOError, (errno, strerror):
        print ("I/O Error(%s) : %s" % (errno, strerror))
        sys.exit(2)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="python file to extract internationalization chains")
    parser.add_argument("output_dir", help="SPIA internationalization file output directory")
    parser.add_argument("-l","--locale", help="Locale of file", default="es-cu")
    parser.add_argument("-f","--function-call", help="Name of the internationalization function in python code", default="_")
    args = parser.parse_args()
    
    input_file = args.input_file
    output_dir = args.output_dir
    locale = args.locale
    
    if locale == None:
        create_chains_file(input_file, output_dir)
    else:
        create_chains_file(input_file, output_dir, lang=locale)
    sys.exit(0)


#logfile = "/media/server-root/home/cccaballero/test/services-manager/src/plugins/apache/__init__.py"
#logfile = "/media/server-root/home/cccaballero/test/git/services-manager/services-manager.py"
#logfile = "/media/server-root/home/cccaballero/test/PSC/PSCkx/psc.py"
#output_dir = "/home/cccaballero/Escritorio/"

#create_chains_file(logfile, output_dir, lang="es-cu")