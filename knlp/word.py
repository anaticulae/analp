# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import nltk.tokenize


def word_tokenize(sentence: str, language='german') -> list:
    """\
    >>> word_tokenize('Ein Aufzählung z.B. heute oder morgen 1. Frosch.')
    ['Ein', 'Aufzählung', 'z.B.', 'heute', 'oder', 'morgen', '1', '.', 'Frosch', '.']
    >>> word_tokenize('Hier lässt sich auch der Luhmann’sche Personenbegriff angliedern.', language='science')
    ['Hier', 'lässt', 'sich', 'auch', 'der', 'Luhmann’sche', 'Personenbegriff', 'angliedern', '.']
    """
    sentence = escape(sentence)
    tokenized = nltk.tokenize.word_tokenize(sentence, language=language)
    result = deescape(tokenized)
    return result


ESCAPE = """\
’sche           QUOTATION_SCHE              # Luhmann’sche, Luhmann’schen
’SCHE           QUOTATION_SCHE_UPPER
'sche           QUOTATION_SCHE_SINGLE
'SCHE           QUOTATION_SCHE_UPPER_SINGLE
"""
ESCAPE: dict = {
    line.split()[0]: line.split()[1] for line in ESCAPE.strip().splitlines()
}


def escape(text: str):
    for key, value in ESCAPE.items():
        text = text.replace(key, value)
    return text


def deescape(text: list):
    # escape mann_sche
    for key, value in ESCAPE.items():
        text = [item.replace(value, key) for item in text]
    return text
