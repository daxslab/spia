from spia.internationalizator import force, load_locale_chains, _

def test_i18n(datadir):
    force('es-cu')
    load_locale_chains(str(datadir.join('')))

    assert _('home') == 'casa'
    assert _('language') == 'idioma'
    assert _('car') == 'auto'
    assert _('home %s', 35) == 'casa 35'

