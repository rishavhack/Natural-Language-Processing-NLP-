# Install NLTK

If you are using Windows or Linux or Mac, you can install NLTK using pip:**pip install nltk**
```
import nltk
nltk.download()
```

# Lexicon Normalization

### The most common lexicon normalization practices are :

>Stemming:  Stemming is a rudimentary rule-based process of stripping the suffixes (“ing”, “ly”, “es”, “s” etc) from a word.
* Word representations may not have any meaning
* Takes less time
* Use stemming when meaning of words is not important for analysis.Example: Spam detection.

>Lemmatization: Lemmatization, on the other hand, is an organized & step by step procedure of obtaining the root form of the word, it makes use of vocabulary (dictionary importance of words) and morphological analysis (word structure and grammar relations).
* Word representations have meaning.
* Takes more time than stemming
* Use lemmatization when meaning of words is important for analysis.Example:Question answering application