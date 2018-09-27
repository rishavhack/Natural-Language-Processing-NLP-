from sklearn.navie_bayes import MultinomialNB
import pandas as pd
import numpy as np

data = pd.read_csv('spambase.data').as_matrix()