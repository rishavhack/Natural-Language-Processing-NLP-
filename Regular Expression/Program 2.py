import re
sentence = "I was born in the year 1996"

re.match(r".*",sentence)
re.match(r".+",sentence)

re.match(r"[a-zA-Z]+",sentence)

sent = "a"
ab = re.match(r"ab?",sent)
print ab