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

# Bag-of-Words Model
>The bag-of-words model is simple to understand and implement and has seen great success in problems such as language modeling and document classification.


# TF-IDF Model
```
TF = Term Frequency
IDF = Inverse Document Frequency
TF-TDF = TF*IDF
```

```
# Formula
Term Frequency = (No. pf occurrences of a word in a document)/(No. of words in that particular document)

Example - "to be or not to be"
1. to = 1+1/6 =0.33
2. be = 0.33
3. or =0.16


IDF = log((No.of documents)/(No. of document containing word))
Example - "to be or not to be"."i have to be"."you got to be"
1. to = log(3/3) = 0
2. have = log(3/1) 
3. be = log(3/3)

```

# N-Gram
>An N-Gram is a contiguous sequence of n items from a given sample of text or speech.
>Items refer to states in ***Markov Chains***.Items can be "Characters","Words","sentences" etc
 ## Example
 ```
 N = 2 then bigrams
 N = 3 then trigrams
 and so on
 
 Example - "the bird is flying on the  blue sky"
 N = 2
 Character Bigrams = 'th','he','e ',' b','bi','ir','rd','d ',' i'..etc.
 N = 3
 Character Trigrams = 'the','he ','e b',' bi','bir','ird' etc

 Word Gram Trigram - 'the bird is', 'bird is flying', 'is flying on' etc

 ```

## Latent Semantic Analysis
>**Latent Semantic Analysis** is a technique of analysing relationships between a set of dcouments and the terms they contain by producing a set of concepts related to the documents and terms.

### SVD(Singular Value decomposition) - Definition
```
A[m*n] = U[m*r] * S[r*r] * (V[n*r])^T

* A: Input Data Matrix
	- m * n matrix (m = number of documents,n = number of words/features)
* U: Left Singular matrix
	- m * r matrix (m = number of documents,r = number of concepts)
* S:Rank Matrix
	- r * r matrix (r = rank of A)
* V:Right Singular Matrix
	- n *r matrix (n = number of words/features, r = number of concepts)
```
* Latent Semantic Analysis - Application
	- Article Bucketing in Websites
	- Finding relations between articles/words
	- Page Indexing in Search Engines