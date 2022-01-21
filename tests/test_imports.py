# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================


def test_import_stopwords_lazy():
    import knlp
    assert len(knlp.__lazy__.STOPWORDS) > 100
    assert len(knlp.STOPWORDS) > 100


def test_import_stopwords_from_module():
    import knlp
    assert len(knlp.STOPWORDS) > 100
