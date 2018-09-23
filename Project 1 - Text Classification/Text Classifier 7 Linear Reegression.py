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

# Creating the corpus
corpus = []
for i in range(0,len(x)):
    review = re.sub(r'\W',' ',str(x[i]))
    review = review.lower()
    review = re.sub(r'\s+[a-z]\s+',' ',review)
    review = re.sub(r'^[a-z]\s+',' ',review)
    review = re.sub(r'\s+',' ',review)
    corpus.append(review)


#Method of BOW Model
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(max_features=2000,min_df=1,max_df=0.6,stop_words = stopwords.words('english'))
x = vectorizer.fit_transform(corpus).toarray()


#Method to create TFIDF from bOW
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
x = transformer.fit_transform(x).toarray()

from sklearn.model_selection import train_test_split
text_train,text_test,sent_train,sent_test = train_test_split(x,y,test_size=0.2,random_state=0)


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(text_train,sent_train)


sent_pred = classifier.predict(text_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(sent_test,sent_pred)