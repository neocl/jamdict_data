# Jamdict database

A precompiled database that contains Jim Breen's JMdict, KanjiDic2, KRADFILE and JMnedict.

This package is intended for using with [jamdict](https://pypi.org/project/jamdict/) package.
For more information, please visit:

- Jamdict documentation: https://jamdict.readthedocs.io/
- Jamdict on PyPI: https://pypi.org/project/jamdict/
- Jamdict source code: https://github.com/neocl/jamdict/
- Dictionary source files are available on: https://www.edrdg.org/wiki/

Compiled date: 17 Apr 2021

## Installation

`jamdict-data` is available on PyPI and can be installed with:

```bash
pip install jamdict-data
```

The database is also available on Google Drive:

https://drive.google.com/drive/u/1/folders/1z4zF9ImZlNeTZZplflvvnpZfJp3WVLPk

## Development

1. Compile Jamdict database file `jamdict.db` using jamdict library
2. Compress the database using xz
3. Copy `jamdict.db.xz` into `jamdict_data` package folder and run sdist command

```bash
python3 setup.py sdist
```

## Dictionaries license

All dictionaries in this package are licensed under CC BY-SA 3.0.

Read more here: https://www.edrdg.org/edrdg/licence.html
