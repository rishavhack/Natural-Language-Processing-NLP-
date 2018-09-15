import nltk


paragraph = """The Taj Mahal was built by Emperor Shah Jahan"""

words = nltk.word_tokenize(paragraph)

tagged_words = nltk.pos_tag(words)

nameEntiy = nltk.ne_chunk(tagged_words)
namedEnt.draw()
