import nltk
from nltk.stem import PorterStemmer

paragraph ="John does his work intelligently. John is an intelligent man. John  is always working"
sentences = nltk.word_tokenize(paragraph)
stemmer = PorterStemmer() #Create Object
print sentences;
for w in sentences:
    print "Actual %s || Stem: %s",w,stemmer.stem(w)