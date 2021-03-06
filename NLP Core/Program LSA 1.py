
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD

dataset = ["The amount of polution is increasing day by day",
           "The concert was just great",
           "I love to see Gordon Ramsay cook",
           "Google is introducing a new technology",
           "AI Robots are examples of great technology present today",
           "All of us were singing in the concert",
           "We have launch campaigns to stop pollution and global warming"]


dataset = [line.lower() for line in dataset]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset)


lsa = TruncatedSVD(n_components = 4, n_iter = 100)
lsa.fit(X)
row1 = lsa.components_[0]
terms = vectorizer.get_feature_names()

for i,comp in enumerate(lsa.components_):
    componentTerms = zip(terms,comp)
    sortedTerms = sorted(componentTerms,key=lambda x:x[1],reverse=True)
    sortedTerms = sortedTerms[:10]
    print "\nConcept",i,":"
    for term in sortedTerms:
        print term