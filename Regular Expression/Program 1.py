import re

sentence = "I was born in 1996";

re.match(r".*",sentence)
re.match(r".+",sentence)

re.match(r"[a-zA-Z]+",sentence)