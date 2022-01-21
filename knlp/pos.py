# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import knlp
import knlp.__lazy__


def sent_pos(text: str, language='german') -> list:
    """\
    >>> sent_pos('Helmut is speaking.', language='eng')
    [('Helmut', 'NNP'), ('is', 'VBZ'), ('speaking', 'VBG'), ('.', '.')]
    >>> sent_pos('Hier spricht Helmut.') # TODO: not supported yet
    """
    language = lang(language)
    tokens = knlp.word_tokenize(text)
    try:
        tagged = knlp.__lazy__.pos_tag(tokens, lang=language)
    except NotImplementedError:
        utila.error(f'language not supported: {language}')
        return None
    return tagged


def lang(item: str) -> str:
    item = item.replace('german', 'ger')
    item = item.replace('english', 'eng')
    return item
