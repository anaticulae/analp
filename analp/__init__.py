#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import importlib.metadata
import os

import analp.__lazy__
from analp.pos import sent_pos
from analp.sentence import normalize as normalize_sentence
from analp.sentence import sent_tokenize
from analp.sentiment import sent_sentiment
from analp.word import isstopword
from analp.word import stopwords
from analp.word import word_tokenize

# import german_data
# import ltk_data

PACKAGE = 'analp'
__version__ = importlib.metadata.version(PACKAGE)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
"""Load STOPWORDS on access time."""
# from analp.corpus import STOPWORDS, see __lazy__
__getattr__ = lambda name: getattr(analp.__lazy__, name)

# ltk_data.add_nltk_path(german_data.ROOT)
