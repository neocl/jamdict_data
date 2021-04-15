# Jamdict database

A precompiled database that contains Jim Breen's JMdict, KanjiDic2, KRADFILE and JMnedict.

This package is intended for using with [jamdict](https://pypi.org/project/jamdict/) package.
For more information, please visit:

- Jamdict documentation: https://jamdict.readthedocs.io/
- Jamdict on PyPI: https://pypi.org/project/jamdict/
- Jamdict source code: https://github.com/neocl/jamdict/

## Installation

jamdict_data is available on PyPI and can be installed with:

```bash
pip install jamdict jamdict_data
```

## Development

Copy database file `jamdict.db` into `jamdict_data` package folder before compiling with the following command

```bash
python3 setup.py sdist --formats=xztar
```

## Dictionaries license

All dictionaries in this package are licensed under CC BY-SA 3.0.

Read more here: https://www.edrdg.org/edrdg/licence.html
