# -*- coding: utf-8 -*-
"""Text Cleaning and Preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aHZ5LlG9RUUKQnGJ5e04wGYKFQfVJTEI

Complet Text Processing

## general Feature Extraction




*   File loading
*   Word counts
*   Characters count
*   Average characters per word
*   Stop words cound
*   Count #HashTags and @Mentions
*   If numeric digits are present in twits
*   Upper case word counts

# Preprocessing and Cleaning

* Lower case
* Contraction and Expansion
* Emails removal and counts
* Removal of RT
* Removal of Special Characters
* Removal of multiple spaces
* Removal of HTML tags
* Removal of accented characters
* Removal of Stop words
* Conversion into base form of words
* Common Occuring words Removal
* Rare Occuring words Removal
* Word Cloud
* Spelling Correction
* Tokenization
* Lemmatizatin
* Noun Detection
* Language Detection
* Sentence Translation
* Using inbuilt Sentiment Classifier
"""

import pandas as pd
import numpy as np
import spacy

from spacy.lang.en.stop_words import STOP_WORDS as stopwords

df = pd.read_csv('https://raw.githubusercontent.com/laxmimerit/twitter-data/master/twitter4000.csv', encoding = 'latin1')

df.head()

df['sentiment'].value_counts()

"""0 - negative
 1 - positive sentiment

# Word Counts

Ile slow mamy w kazdym zdaniu w kazdym wierszu
"""

len('this is text') #liczy znaki

len('this is text'.split())

df['word_counts'] = df['twitts'].apply(lambda x: len(str(x).split()))

df.head(5)

df['word_counts'].min()

df['word_counts'].max()

df[df['word_counts']==1]

"""# Characters Count"""

len('this is')
#to liczy dodatkowo spacje

def char_counts(x):
  s = x.split()
  x = ''.join(s)
  return len(x)

char_counts('this is')

df['char_counts'] = df['twitts'].apply(lambda x:char_counts(str(x)))

df.head()

"""# Average Word Length"""

x = 'this is'# 6 (characters) / 2(wrrds) = 3
y = 'thankyou guys' #12/2 = 6

df['avg_word_len'] = df['char_counts'] / df['word_counts']

df.head()

"""# Stop words

Stop Words - are those words which occurs very frequently in the text corpus

potrafia stanowic nawet 30/40/50% calego tekstu
"""

print(stopwords)

len(stopwords)

x = 'this is the text data'
x.split()

[t for t in x.split() if t in stopwords]

df['stop_words_len'] = df['twitts'].apply(lambda x:len([t for t in x.split() if t in stopwords]) )

df.head()

"""# Count #HashTags and @Mentions"""

x = 'this is #hashtag and this is @mention'

x.split()

[t for t in x.split() if t.startswith('#')]

[t for t in x.split() if t.startswith('@')]

df['hashtags_count'] = df['twitts'].apply(lambda x: len([t for t in x.split() if t.startswith('#')]))

df['mentions_count'] = df['twitts'].apply(lambda x: len([t for t in x.split() if t.startswith('@')]))

df.head()

"""# Numeric Digit Count"""

x = 'this is 1 and 2'

x.split()

x.split()[3].isdigit()

df['numerics_count'] = df['twitts'].apply(lambda x: len([t for t in x.split() if t.isdigit()]))

df.head()

"""# UPPER CASE WORDS COUNT

Why we need this counter?

When something is written in uppercase, then there is an amotion in that part
positive or negative
"""

x = 'I AM HAPPY'
y = 'i am happy'

[t for t in y.split() if t.isupper()]

[t for t in x.split() if t.isupper()]

df['upper_counts'] = df['twitts'].apply(lambda x: len([t for t in x.split() if t.isupper()]))

df.head()

df.iloc[3962]['twitts']

"""# Preprocessing and Cleaning

## Lower Case Conversion
"""

x = 'this is Text'

x.lower()

x = 45
str(x).lower()

df['twitts'] = df['twitts'].apply(lambda x: str(x).lower())

df.head()

"""# Contraction to Expansion

ta liste wzial z wiki.
Tutaj chodzi o to, aby wszystkie skrocone formy wypowiedzi, przekonwertowac na dluzsze
"""

contractions = {
"ain't": "am not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how does",
"i'd": "i would",
"i'd've": "i would have",
"i'll": "i will",
"i'll've": "i will have",
"i'm": "i am",
"i've": "i have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that would",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
" u ": " you ",
" ur ": " your ",
" n ": " and ",
"won't": "would not",
'dis': 'this',
'bak': 'back',
'brng': 'bring'}

x = "i'm don't he'll" # "i am do not he will"

def cont_to_exp(x):
    if type(x) is str:
        for key in contractions:
            value = contractions[key]
            x = x.replace(key, value)
        return x
    else:
        return x

cont_to_exp(x)

# Commented out IPython magic to ensure Python compatibility.
# %%timeit
# #dziala to w jupyterze i pokazuje  ile czasu na to potzreba
# df['twitts'] = df['twitts'].apply(lambda x: cont_to_exp(x))

df.head()

"""# Count and Remove Emails"""

df[df['twitts'].str.contains('hotmail.com')]

df.iloc[3713]['twitts']

x = '@securerecs arghh me please  markbradbury_16@hotmail.com'

import re

# chcemy usunac ze stringa w x nazwe email, gdyz jest to dana wrazliwa
#szukamy przez to pattern
re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)', x)
# [a-z0-9+._-] - litery od a do z i cyfry od 0-9
# + znacza anything
# [a-z0-9+._-] jest to zakodowanie tego ostat

df['emails'] = df['twitts'].apply(lambda x: re.findall(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+\b)', x))

df['emails_count'] = df['emails'].apply(lambda x:len(x))

df[df['emails_count']>0]

re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x)

df['twitts'] = df['twitts'].apply(lambda x: re.sub(r'([a-z0-9+._-]+@[a-z0-9+._-]+\.[a-z0-9+_-]+)',"", x))

df[df['emails_count']>0]

"""# Count URLs and Remove it"""

x = 'hi, thanks to watching it. for more visit https://youtube.com/kgptalkie'

re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)

df['url_flags'] = df['twitts'].apply(lambda x: len(re.findall(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', x)))

df[df['url_flags']>0]

re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x)

df['twitts'] = df['twitts'].apply(lambda x: re.sub(r'(http|https|ftp|ssh)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', '' , x))

df.head()

"""# Remove RT"""

x = 'RT: hello hi'

x = 'rt @username: hello hirt'

df[df['twitts'].str.contains('rt')]

re.sub(r'\brt\b', '', x).strip()

df['twitts'] = df['twitts'].apply(lambda x: re.sub(r'\brt\b', '', x).strip())

"""# Special Chars removal or punctuaction removal"""

x = '@duyku apparently i was not ready enough... i...'

"""# tych kropeczek sie pozbedziemy"""

re.sub(r'[^\w ]+', "", x)

df['twitts'] = df['twitts'].apply(lambda x: re.sub(r'[^\w ]+', "", x))

df.head()

"""# Remove multiple spaces "hi hello "
"""

x =  'hi    hello     how are you'

' '.join(x.split())

df['twitts'] = df['twitts'].apply(lambda x: ' '.join(x.split()))

"""# Remove HTML tags"""

!pip install beautifulsoup4

from bs4 import BeautifulSoup

x = '<html><h1> thanks for watching it </h1></html>'

x.replace('<html><h1>','').replace('</h1></html>','')

BeautifulSoup(x, 'lxml').get_text().strip()
#lxml - pakiet z bs4 ktory utomatycznie usuwa html z tekstu

# Commented out IPython magic to ensure Python compatibility.
# %%time
# df['twitts'] = df['twitts'].apply(lambda x: BeautifulSoup(x,'lxml').get_text().strip())

"""# Remove Accented Chars"""

x = 'Áccěntěd těxt'

import unicodedata

def remove_accented_chars(x):
    x = unicodedata.normalize('NFKD', x).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return x

    # ('ascii', 'ignore') if its ascii,ignore it
    #

remove_accented_chars(x)

df['twitts'] = df['twitts'].apply(lambda x:remove_accented_chars(x))

"""# Remove Stop Words"""

x = 'this is a stop words'

' '.join([t for t in x.split() if t not in stopwords])

df['twitts_no_stop'] = df['twitts'].apply(lambda x: ' '.join([t for t in x.split() if t not in stopwords]))

"""# Convert into base or root form of word"""

nlp = spacy.load('en_core_web_sm')

x = 'this is chocolates. what is times? this balls'
#root words: chocolate, time, ball

def make_to_base(x):
  x = str(x)
  x_list =[]
  doc = nlp(x)

  for token in doc:
    lemma = token.lemma_
    if lemma == '-PRON-' or lemma == 'be':
      lemma = token.text

    x_list.append(lemma)
  return ' '.join(x_list)

make_to_base(x)

df['twitts'] = df['twitts'].apply(lambda x: make_to_base(x))

df.head()

"""# Common words removal

chcemy sprawdzic, ktore slowa wystepuja u nas najwiecej razy
"""

x = 'this is this okay bye'

#joining all rows into a single long text
text = ' '.join(df['twitts'])

text

len(text)

text = text.split()

len(text)

pd.Series(text)

freq_common = pd.Series(text).value_counts()
freq_common

f20 = freq_common[:20]

f20

# next im going to remove this stop words from our text data

df['twitts'] = df['twitts'].apply(lambda x: ' '.join([t for t in x.split() if t not in f20]))

df.head()

"""# Rare words removal

Czesto je wywalamy, bo sa nimi czesto wyrazy z bledami
"""

rare20 = freq_common.tail(20)

rare20

df['twitts'] = df['twitts'].apply(lambda x: ' '.join([t for t in x.split() if t not in rare20]))

"""# Word Cloud Visualization"""

!pip install wordcloud

# Commented out IPython magic to ensure Python compatibility.
from wordcloud import WordCloud
import matplotlib.pyplot as plt
# %matplotlib inline

text = ' '.join(df['twitts'])

wc = WordCloud(width=800, height=400).generate(text)
plt.imshow(wc)
plt.axis('off')
plt.show()

"""w tej grafice wysiwetlaja sie slowa, ktore naczesciej wystepuja w naszym zbiorze

# Spelling Correction
"""

!pip install -U textblob

!python -m textblob.download_corpora

from textblob import TextBlob

x = 'thankks forr waching it'

x = TextBlob(x).correct()

x

"""# Tokenization using TextBlob"""

x = 'thanks#watching this video. please like it'

TextBlob(x).words

doc = nlp(x)
for token in doc:
  print(token)

"""# Detecting Nouns"""

x = 'Breaking News: Donal Trump, the president of the USA is looking to sign a deal to mine the moon'

doc = nlp(x)

for noun in doc.noun_chunks:
  print(noun)

"""# Language Translation and Detection

Language Code: https://www.loc.gov/standards/iso639-2/php/code_list.php
"""

x

tb = TextBlob(x)

#how to detect language:
#tb.detect_language()

#how to transalte our text to another language
# tb.translate(to='fr')
#fr- francuski
## tb.translate(to='hi') hinduski

"""# Use TextBlob's inbuilt Sentiment Classifier"""

from textblob.sentiments import NaiveBayesAnalyzer

x = 'we all stands together. we are gonna win this fight'

tb = TextBlob(x, analyzer=NaiveBayesAnalyzer())

tb.sentiment

x = '''i don't understand why you believe her'''
tb = TextBlob(x, analyzer=NaiveBayesAnalyzer())
tb.sentiment

"""# Other Resources
|  ML Course | Description |
|:---|:---|
| [**Data Visualization in Python Masterclass™: Beginners to Pro**](https://bit.ly/udemy95off_kgptalkie) |  Learn to build Machine Learning and Deep Learning models using Python and its libraries like Scikit-Learn, Keras, and TensorFlow. |
| [**Python for Machine Learning: A Step-by-Step Guide**](https://bit.ly/ml-ds-project) | Learn to build Machine Learning and Deep Learning models using Python and its libraries like Scikit-Learn, Keras, and TensorFlow. |
| [**Python for Linear Regression in Machine Learning**](https://bit.ly/regression-python) | Learn to build Linear Regression models using Python and its libraries like Scikit-Learn. |
| [**Introduction to Spacy 3 for Natural Language Processing**](https://bit.ly/spacy-intro) | Learn to build Natural Language Processing models using Python and its libraries like Spacy. |
| [**Advanced Machine Learning and Deep Learning Projects**](https://bit.ly/kgptalkie_ml_projects) | Learn to build Advanced Machine Learning and Deep Learning models using Python and transformer models like BERT, GPT-2, and XLNet. |
| [**Natural Language Processing in Python for Beginners**](https://bit.ly/intro_nlp) | Learn to build Natural Language Processing Projects using Spacy, NLTK, and Gensim, and transformer models like BERT, GPT-2, and XLNet. |
| [**Deployment of Machine Learning Models in Production in Python**](https://bit.ly/bert_nlp) |  Learn to deploy Machine Learning and Deep Learning models using Python and its libraries like Flask, Streamlit, and NGINX. |
| [**R 4.0 Programming for Data Science - Beginners to Pro**](https://bit.ly/r4-ml) | Learn to build Machine Learning and Deep Learning models using R and its libraries like caret, tidyverse, and keras. |

"""

