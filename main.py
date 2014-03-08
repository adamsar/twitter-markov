from twitter_markov import twitter, data
from twitter_markov.markov import generate_text
from nltk.corpus import shakespeare

all_words = " ".join(reduce(lambda x, y: x + y, [shakespeare.words(f) for f in shakespeare.fileids()]))

print generate_text(all_words)
