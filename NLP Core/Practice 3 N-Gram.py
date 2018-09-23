import random
import nltk

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n = 3
 
ngrams = {}
 
 # Create the n-grams
for i in range(len(text)-n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n])
     
currentGram = text[0:n]
result = currentGram
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += nextItem
    currentGram = result[len(result)-n:len(result)]
    
print result

wgrams = {}

words = nltk.word_tokenize(text)
for i in range(len(words)-n):
    gram = ' '.join(words[i:i+n])
    if gram not in wgrams.keys():
        wgrams[gram] = []
    wgrams[gram].append(words[i+n])
    
currentWordGram = ' '.join(words[0:n])
result = currentWordGram
for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibilities = wgrams[currentWordGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += ' '+nextItem
    rwords = nltk.word_tokenize(result)
    currentWordGram = ' '.join(rwords[len(rwords)-n:len(rwords)])
    
print result