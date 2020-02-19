#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lexical disperssion plots and concordance of select words based on Bag of Words list.

@author: owenbezick
"""

import os
import nltk
from nltk import Text
#import file
filename_text = "VirginiaVSPurdue.txt"
cwd = os.getcwd()
filepath_text = os.path.join(cwd, filename_text)
nltk_text = Text(nltk.corpus.gutenberg.words(filepath_text))
nltk_text.concordance("virginia")

nltk_text.similar('shot')
nltk_text.dispersion_plot(["win", "Virginia", "Purdue"])

nltk_text = Text(nltk.corpus.gutenberg.words(filepath_text))
nltk_text.concordance("virginia")
nltk_text.similar('shot')
nltk_text.dispersion_plot(["win", "Virginia", "Purdue"])