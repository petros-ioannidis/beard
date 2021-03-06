# -*- coding: utf-8 -*-
#
# This file is part of Beard.
# Copyright (C) 2015 CERN.
#
# Beard is a free software; you can redistribute it and/or modify it
# under the terms of the Revised BSD License; see LICENSE file for
# more details.

"""Helper functions for strings.

.. codeauthor:: Gilles Louppe <g.louppe@cern.ch>

"""

import unicodedata
import sys

IS_PYTHON_3 = sys.version_info[0] == 3


def asciify(string):
    """Transliterate a string to ASCII."""
    if not IS_PYTHON_3 and not isinstance(string, unicode):
        string = unicode(string, "utf8", errors="ignore")

    string = unicodedata.normalize("NFKD", string)
    string = string.encode("ascii", "ignore")
    string = string.decode("utf8")

    return string
