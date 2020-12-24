import nltk
nltk.download()
from nltk.corpus import stopwords
import csv
from nltk.tag import pos_tag # for proper noun
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
import pandas as pd
import math
ps = PorterStemmer()