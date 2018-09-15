import nltk
from nltk.corpus import stopwords

en_stops = set(stopwords.words('english'))
words = ['There','is','a','tree','near','the','river']
for word in words:
    if word not in en_stops:
        print word
