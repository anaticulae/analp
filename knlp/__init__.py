#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import os

import knlp.__lazy__
from knlp.pos import sent_pos
from knlp.sentence import normalize as normalize_sentence
from knlp.sentence import sent_tokenize
from knlp.sentiment import sent_sentiment
from knlp.word import isstopword
from knlp.word import stopwords
from knlp.word import word_tokenize

__version__ = '0.6.1'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
"""Load STOPWORDS on access time."""
# from knlp.corpus import STOPWORDS, see __lazy__
__getattr__ = lambda name: getattr(knlp.__lazy__, name)
