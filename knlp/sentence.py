# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import string

import nltk.stem

STEMMER = nltk.stem.SnowballStemmer("german")


def normalize(raw: str, remove_punctation: bool = True) -> str:
    """\
    >>> normalize('Hier spricht Helmut .')
    'hier spricht helmut'
    >>> normalize('Heute sprechen wir doch über ein Thema')
    'heut sprech wir doch uber ein thema'
    """
    raw = raw.lower()
    splitted = raw.split()
    if remove_punctation:
        splitted = [item for item in splitted if item not in string.punctuation]
    stemmed = [STEMMER.stem(item) for item in splitted]
    result = ' '.join(stemmed)
    return result
