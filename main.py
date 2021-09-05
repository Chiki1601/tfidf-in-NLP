# import and instantiate TfidfVectorizer (with the default
parameters)
from sklearn.feature_extraction.text import TfidfVectorizer
vect = TfidfVectorizer()
vect
# use TreeankWordTokenizer
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
vect.set_params(tokenizer=tokenizer.tokenize)
# remove English stop words
vect.set_params(stop_words=&#39;english&#39;)

# include 1-grams and 2-grams
vect.set_params(ngram_range=(1, 2))
# ignore terms that appear in more than 50% of the documents
vect.set_params(max_df=0.5)
# only keep terms that appear in at least 2 documents
vect.set_params(min_df=2)
