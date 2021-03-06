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
    """
    tokenized = nltk.tokenize.word_tokenize(sentence, language=language)
    return list(tokenized)
