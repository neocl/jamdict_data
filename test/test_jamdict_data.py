#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Le Tuan Anh <tuananh.ke@gmail.com>"
__copyright__ = "Copyright 2021, jamdict_data"
__license__ = "MIT"

import unittest
import jamdict_data
from pathlib import Path


class TestJamdictData(unittest.TestCase):

    def test_get_path(self):
        actual = Path(jamdict_data.JAMDICT_DB_PATH)
        self.assertEqual(actual.name, 'jamdict.db')
        self.assertTrue(actual.exists())


if __name__ == "__main__":
    logging.getLogger('jamdict_data').setLevel(logging.DEBUG)
    unittest.main()
