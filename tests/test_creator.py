from spia.creator import *
from os import makedirs

def test_create_i18n_file(datadir):

    test_file = str(datadir.join('test.py'))
    test_lang_dir = str(datadir.join('lang'))
    test_generated_int_file = str(datadir.join('lang', 'es-cu.py'))


    makedirs(test_lang_dir)
    create_chains_file(test_file, test_lang_dir, lang = "es-cu")

    a = open(test_generated_int_file)
    b = a.read()
    a.close()

    assert  "'lolo':'lolo'," in b
    assert  "'pepe':'pepe'," in b
    assert  "'loloa':'loloa'," in b