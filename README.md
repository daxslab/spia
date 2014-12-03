**SPIA, simple python internationalization api**
================

Quickly and easy, internationalize your python applications

**About**

SPIA makes easy the internationalization process in a on-growing python application, with a pure python (and pythonic) internationalization.
**SPIA is not a complete i18n API yet, but maybe in the future... well, it maybe is not an api yet...**

**SPIA is now python 3.x compatible**

How it works
================

**Internationalization files**

The SPIA internationalization files are python modules that contains a dictionary with the key-text peers, the module names correspond to a simplified locale name, for example: "en-us.py" for United States english or "es-es.py" for Spain spanish, this is an example of a es-es.py content:

```python
# coding: utf8

keys = {
'home' : 'casa',
'keyboard' : 'teclado',
'computer' : 'computadora',
'my name is %s' : 'mi nombre es %s'
}
```
SPIA can find the correct module for the system locale and replace the code keywords for the correct translated strings.

**Python code**

This is an example of a python application using SPIA:

```python
import spia.internationalizator as internationalizator # import the SPIA internationalizator
from spia.internationalizator import _ # import the internationalization function, IN THIS CASE: _()
"""
For another function caller (for example T):
from spia.internationalizator import _ as T
"""

internationalizator.load_locale_chains("/app/locale_dir") # the locale dir contains the internationalization files

print _('home')
print _('keyboard')
print _('computer')
print _('my name is %s', 'Pepe')
```
Output in a spanish eviroment:
```
casa
teclado
computadora
mi nombre es Pepe
```
Output in a english eviroment:
```
home
keyboard
computer
my name is Pepe
```

To force a defined locale you could use:
```python
internationalizator.force('es-es') # force translation to Spain spanish
internationalizator.force('es_ES') # same
internationalizator.force('es') # force translation to spanish
internationalizator.force(None) # back to use enviroment locale
# or
internationalizator.force('') # back to use enviroment locale
```

**Creator**

SPIA has a creator module (or script), that create or update the locale files (internationalization files) for you, it obtain the internationalization strings (by default the _('string') function) from a python file, and create (or update) the locale module specified with the -l option. we can use it in that way:

    python creator.py my_python_file.py /my_locales_folder/ -l es-es

A different function call can be specified with the -f option, for example, for use the T('string') function call:

    python creator.py my_python_file.py /my_locales_folder/ -l es-es -f T

