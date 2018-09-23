import numpy as numpy
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files


reviews = load_files('txt_sentoken/')
x,y = reviews.data,reviews.target