import numpy as numpy
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files


reviews = load_files('txt_sentoken/')
x,y = reviews.data,reviews.target

#Storing as Pickle Files (wb = write byte)
with open('X.pickle','wb') as f:
    pickle.dump(x,f)

with open('Y.pickle','wb') as f:
    pickle.dump(y,f)
    
#Unpickling the dataset
with open('X.pickle','rb') as f:
    x = pickle.load(f)

with open('Y.pickle','rb') as f:
    y = pickle.load(f)
    