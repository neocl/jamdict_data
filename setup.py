#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Setup script for jamdict_data

Latest version can be found at https://github.com/neocl/jamdict_data

:copyright: (c) 2021 Le Tuan Anh <tuananh.ke@gmail.com>
:license: MIT, see LICENSE for more details.
'''

import os
import sys
import io
import lzma
from setuptools import setup
from setuptools.command.install import install


def _unpack_db():
    # unpack database package after installed
    ZIPPED_DB = os.path.abspath("jamdict_data/jamdict.db.xz")
    TARGET_DB = os.path.abspath("jamdict_data/jamdict.db")
    if os.path.isfile(ZIPPED_DB) and not os.path.isfile(TARGET_DB):
        print(f"Unpacking database from {ZIPPED_DB} to {TARGET_DB}")
        with lzma.open(ZIPPED_DB) as f:
            db_content = f.read()
            with open(TARGET_DB, "wb") as out:
                out.write(db_content)
            # delete the xz file
            os.unlink("jamdict_data/jamdict.db.xz")


class InstallUnpackDatabase(install):
    def run(self):
        super().run()
        _unpack_db()


_cmdclass = {'install': InstallUnpackDatabase}

try:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
    class BuildDatabase(_bdist_wheel):
        def finalize_options(self):
            super().finalize_options()
            _unpack_db()
    _cmdclass['bdist_wheel'] = BuildDatabase
except ImportError:
    print()
    print("-" * 80)
    print(">>> INSTALL FAILED - BUT FIX IS AVAILABLE BELOW (mostly because of corrupted wheel) <<<")
    print("jamdict_data relies on wheel to unpack data, please make sure that wheel is installed by running `pip install wheel`")
    print("Some systems, like Ubuntu, is shipped with broken wheel in virtual environments! Hopefully this pain will go away soon.")
    print("You may need to uninstall jamdict_data before reinstall it again: `pip uninstall jamdict_data`")
    print("-" * 80)
    print()
    raise
    # wheel is not available ...
    ### class BuildDatabase(install):
    ###     def run(self):
    ###         super().run()
    ###         _unpack_db()
    ### _cmdclass['bdist_wheel'] = BuildDatabase


def read(*filenames, **kwargs):
    ''' Read contents of multiple files and join them together '''
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


# readme_file = 'README.rst' if os.path.isfile('README.rst') else 'README.md'
readme_file = 'README.md'
long_description = read(readme_file)
pkg_info = {}
exec(read('jamdict_data/__version__.py'), pkg_info)


setup(
    name='jamdict_data',  # package file name (<package-name>-version.tar.gz)
    version=pkg_info['__version__'],
    url=pkg_info['__url__'],
    project_urls={
        "Bug Tracker": "https://github.com/neocl/jamdict_data/issues",
        "Source Code": "https://github.com/neocl/jamdict_data/"
    },
    cmdclass=_cmdclass,
    keywords="nlp",
    license=pkg_info['__license__'],
    author=pkg_info['__author__'],
    tests_require=[],
    install_requires=[],
    author_email=pkg_info['__email__'],
    description=pkg_info['__description__'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['jamdict_data'],
    package_data={'jamdict_data': ['jamdict.db']},
    include_package_data=True,
    platforms='any',
    test_suite='test',
    # Reference: https://pypi.opython.org/pypi?%3Aaction=list_classifiers
    classifiers=['Programming Language :: Python',
                 'Development Status :: 2 - Pre-Alpha',
                 'Natural Language :: Japanese',
                 'Environment :: Plugins',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: {}'.format(pkg_info['__license__']),
                 'Operating System :: OS Independent',
                 'Topic :: Database',
                 'Topic :: Text Processing :: Linguistic',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)
