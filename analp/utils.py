# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import unicodedata


def hashed(item: str) -> str:
    """\
    >>> hashed('‘SCHEN')
    'LEFTSINGLEQUOTATIONMARKSCHEN'
    """
    selected = [
        unicodedata.name(char) if ord(char) > 256 else char for char in item
    ]
    selected = ''.join(selected).replace(' ', '')
    return selected


ESCAPE = """\
‘schen
‘SCHEN
’schen
’SCHEN
'schen
'SCHEN
‘sche
’sche
’SCHE
'sche
'SCHE
‘s
‘S
’s
’S
's
'S
"""
ESCAPE: dict = {
    f'{line} ': f'{hashed(line)} ' for line in ESCAPE.strip().splitlines()
}


def escape(text: str):
    for key, value in ESCAPE.items():
        text = text.replace(key, value)
    return text


def deescape(text: list):
    # escape mann_sche
    for key, value in ESCAPE.items():
        text = [item.replace(value.strip(), key.strip()) for item in text]
    return text
