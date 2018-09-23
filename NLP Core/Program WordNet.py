from nltk.corpus import wordnet

synonyms = []
antonyms = []

for syn in wordnet.synsets('good'):
    for s in syn.lemmas():
        synonyms.append(s.name())
        for a in s.antonyms():
            antonyms.append(a.name())
            
print set(synonyms)
print set(antonyms)
