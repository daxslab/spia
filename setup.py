from setuptools import setup

long_description = """\
SPIA
========
Simple Python internationalization API http://spia.readthedocs.io
"""

setup(
    name='spia',
    version='0.1.0',
    packages=['spia', 'spia.creator', 'spia.internationalizator'],
    url='https://github.com/daxslab/spia',
    license='LGPL 3.0',
    author='Carlos Cesar Caballero Diaz',
    author_email='ccesar@daxslab.com',
    description='Simple Python internationalization API',
    long_description=long_description,
    platforms='any',
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    extras_require={
            'dev': [
                'pytest',
                'pytest-pep8',
                'pytest-cov',
                'sphinx',
                'tox'
            ]
        },
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',

        # Pick your license as you wish
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)