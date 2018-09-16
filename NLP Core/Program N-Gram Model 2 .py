import random
import nltk

text = """Global warming or climate change has become a worldwide concern. It is gradually developing into an unprecedented environmental crisis evident in melting glaciers, changing weather patterns, rising sea levels, floods, cyclones and droughts. Global warming implies an increase in the average temperature of the Earth due to entrapment of greenhouse gases in the earth’s atmosphere."""

n = 3

ngrams = {}

words = nltk.word_tokenize(text)

for i in range(len(words)-n):
	gram = ' '.join(words[i:i+n])
	if gram not in ngrams.keys():
		ngrams[gram] = []
	ngrams[gram].append(words[i+n])

currentGram = ' '.join(words[0:n])
result = currentGram
for i in range(30):
	if currentGram not in ngrams.keys():
		break
	possibilites = ngrams[currentGram]
	nextItem = possibilites[random.randrange(len(possibilites))]
	result += ' '+nextItem
	rwords = nltk.word_tokenize(result)
	currentGram = ' '.join(rwords[len(rwords)-n:len(rwords)])

print result