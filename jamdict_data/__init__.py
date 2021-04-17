# -*- coding: utf-8 -*-

'''
Pre-compiled database for jamdict module
Latest version can be found at https://github.com/neocl/jamdict_data

References:
    JMDict website:
        http://www.csse.monash.edu.au/~jwb/edict.html
    Dictionaries licenses:
        http://www.edrdg.org/edrdg/licence.html
    Python documentation:
        https://docs.python.org/
    PEP 257 - Python Docstring Conventions:
        https://www.python.org/dev/peps/pep-0257/

@author: Le Tuan Anh <tuananh.ke@gmail.com>
@license: MIT
'''

# Copyright (c) 2021, Le Tuan Anh <tuananh.ke@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

########################################################################

from .__version__ import __author__, __email__, __copyright__, __maintainer__
from .__version__ import __credits__, __license__, __description__, __url__
from .__version__ import __version_major__, __version_long__, __version__, __status__

import os

MY_FOLDER = os.path.dirname(os.path.abspath(__file__))
JAMDICT_DB_PATH = os.path.join(MY_FOLDER, 'jamdict.db')
