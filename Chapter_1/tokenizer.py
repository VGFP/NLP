# This tokenizer gnores whitespace tokens. It also separates sentence-ending 
# trailing punctuation from tokens that do not contain any other 
# punctuation characters.
# 
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+|$[0-9.]+|\S+')

sentence = 'We’re going to study how to train such a tokenizer and how to manually add abbreviations to fine-tune it.'

tokenized_sen = tokenizer.tokenize(sentence)

# print("RegexpTokenizer")
# print(tokenized_sen)

from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

tokenized_sen = tokenizer.tokenize(sentence)

# print("TreebankWordTokenizer")
# print(tokenized_sen)

# Tokenize informal text from social networks such as Twitter and Facebook
from nltk.tokenize.casual import casual_tokenize

message = """RT @TJMonticello Best day everrrrrrr at Monticello. Awesommmmmmeeeeeeee day :*)"""

tokenized_sen = casual_tokenize(message)

# print("casual_tokenize")
# print(tokenized_sen)

tokenized_sen = casual_tokenize(message, reduce_len=True, strip_handles=True)

# print("casual_tokenize reduce_len")
# print(tokenized_sen)

#  Stop Words
import nltk

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')
'''
print("NLTK:")
print(type(stop_words))
print(len(stop_words))
print(str(stop_words[:12]) + '\n')
'''
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS as sklearn_stop_words
'''
print("sklearn:")
print(type(sklearn_stop_words))
print(len(sklearn_stop_words))
'''
#  Stemmer - vocabulary normalization technique that eliminates the small meaning differences of pluralization or possessive endings of words, or even various verb forms
# For example, the words housing and houses share the same stem, house.
import re

def stem(phrase):
    return ' '.join([re.findall('^(.*ss|.*?)(s)?$',word)[0][0].strip("'") for word in phrase.lower().split()])

# print(stem('houses'))
# print(stem("Doctor House's calls"))

from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
# print(' '.join([stemmer.stem(w).strip("'") for w in "dish washer's washed dishes".split()]))

nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer() 
# print(lemmatizer.lemmatize("better", pos="a"))

# Sentiment analyzer
# VADER - Valence Aware Dictionary for sEntiment Reasoning

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer 
sa = SentimentIntensityAnalyzer() 
# print(type(sa.lexicon))
# Length of the lexicon
print(len(sa.lexicon.keys()))
print(sa.lexicon.keys())

test_string = 'Do you live in Warsaw?'
scores = sa.polarity_scores(test_string)
# print(scores)
