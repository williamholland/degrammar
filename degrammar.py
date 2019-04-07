import re
import sys
import nltk
from nltk.stem.wordnet import WordNetLemmatizer

def capitalize(string):
    should_be_capital = True
    result = ''
    for char in string:
        if char in '.!?':
            should_be_capital = True
            result = result + char
        elif should_be_capital and char.isalpha():
            result = result + char.upper()
            should_be_capital = False
        else:
            result = result + char
    return result

text = raw_input()

tokens = nltk.word_tokenize(text)
tags = nltk.pos_tag(tokens)

result = ''
for word, tag in tags:

    if tag in ['DT', 'TO', 'IN', 'RP']:
        continue
    elif word.startswith("'"):
        continue

    if re.match('\w+', tag):
        result = result + ' '

    result = result + WordNetLemmatizer().lemmatize(word, 'v')

print capitalize(result.strip())
