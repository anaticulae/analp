# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import functools

import utila

Configure = collections.namedtuple(
    'Configure',
    'sent_tokenize word_tokenize pos_tag STOPWORDS STEMMER',
)


@functools.lru_cache(maxsize=None)
def lazy() -> Configure:
    utila.debug('configure nltk')
    import nltk
    import nltk.stem
    import nltk.corpus
    result = Configure(
        sent_tokenize=nltk.sent_tokenize,
        word_tokenize=nltk.word_tokenize,
        pos_tag=nltk.pos_tag,
        STOPWORDS=nltk.corpus.stopwords.words('german'),
        STEMMER=nltk.stem.SnowballStemmer("german"),
    )
    return result


def __getattr__(name):
    data = lazy()
    result = getattr(data, name)
    return result
