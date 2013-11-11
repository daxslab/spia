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

import os
import sys
import imp

LOCALE_FOLDER = os.path.join(sys.path[0], "locale")

def load_locale_chains(locale_chains_folder):
    global LOCALE_FOLDER
    LOCALE_FOLDER = locale_chains_folder

def _get_locales_chains_list(locale_chains_folder = None):
    """obtain internationalized chains from folder"""
    locales = []
    if locale_chains_folder == None:
        locale_chains_folder = LOCALE_FOLDER
    if os.path.exists(locale_chains_folder) == False:
        return ""

    internationalization_files = os.listdir(locale_chains_folder)

    # remove non python files
    tmp = []
    for i_file in internationalization_files:
        if i_file[-3:] == ".py":
            tmp.append(i_file)
    internationalization_files = tmp

    for i in internationalization_files:
        try:
            (name, ext) = os.path.splitext(i)        
            if ext == ".py":
                #(file, filename, data) = imp.find_module(name, [locale_chains_folder])
                #module = imp.load_module(name, file, filename, data)
                #locales.append({"locale": i[:-3], "module": module})
                locales.append(_get_module(name,locale_chains_folder))
                #print _get_module(name,locale_chains_folder)
        except:
            pass
    return locales

def _get_module(name, locale_chains_folder):
    """returns a locale module dictionary"""
    (file, filename, data) = imp.find_module(name, [locale_chains_folder])
    module = imp.load_module(name, file, filename, data)
    return {"locale": name[:-3], "module": module}

def _simplify_locale(locale):
    """return a given standard locale string in the SPIA simplified locale format"""
    return locale.split(".")[0].replace("_","-").lower()

def _get_system_locale():
    """Return the system locale"""
    return os.environ["LANG"]

def _get_simple_system_locale():
    """Return a simplified format system locale"""
    return _simplify_locale(_get_system_locale())

def _get_locale_chains(locale_chains_folder = None, locale = ""):
    """return the locale chains object"""
    if not locale == "":
        simple_system_locale = _simplify_locale(locale)
    else:
        simple_system_locale = _get_simple_system_locale()
    if locale_chains_folder == None:
        locale_chains_folder = LOCALE_FOLDER
    locales_chains_list = _get_locales_chains_list(locale_chains_folder)
    locale_chains = ""
    for chain_object in locales_chains_list:
        if simple_system_locale == chain_object["locale"]:
            locale_chains = chain_object
            break
    if locale_chains == "":
        for chain_object in locales_chains_list:
            if simple_system_locale.split("-")[0] == chain_object["locale"]:
                locale_chains = chain_object
    if locale_chains == "":
        for chain_object in locales_chains_list:
            if simple_system_locale.split("-")[0] == chain_object["locale"].split("-")[0]:
                locale_chains = chain_object
    return locale_chains

def apply_replace_rules(chain, args):
    """replaces in chain the %s with the args list"""
    try:
        chain = chain.replace("%s","{!s}")
        chain = chain.format(*args)
    except:
        pass
    return chain

def _(chain, *args, **keys):
    try:
        locale_chains_folder = keys ['locale_chains_folder']
    except:
        locale_chains_folder = None
    try:
        locale = keys['locale']
    except:
        locale = ""

    if locale_chains_folder == None:
        locale_chains_folder = LOCALE_FOLDER
    if locale == "":
        locale = _get_simple_system_locale()
    locale_chains_object = _get_locale_chains(locale_chains_folder = locale_chains_folder, locale = locale)
    locale_chains = locale_chains_object["module"]
    keys = getattr(locale_chains, "keys")
    try:
        internationalized_string = keys[chain]
    except:
        internationalized_string = chain
    
    internationalized_string = apply_replace_rules(internationalized_string, args)
    
    return internationalized_string


#load_locale_chains("/home/cccaballero/test/SPIA/lang")
#print _("home %s", "loca")
#print(_("home %s", "loca"))