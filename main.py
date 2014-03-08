from twitter_markov import twitter_util, data
from twitter_markov.markov import generate_text
from nltk.corpus import shakespeare
import twitter

#all_words = " ".join(reduce(lambda x, y: x + y, [shakespeare.words(f) for f in shakespeare.fileids()]))

#print generate_text(all_words)
key, secret, akey, asecret = twitter_util.get_creds()
client = twitter.Api(
    consumer_key = key,
    consumer_secret = secret,
    access_token_key = akey,
    access_token_secret = asecret)
seed_words = data.TrendingTwitterPool(client).get_training_data()
text = generate_text(seed_words)
client.PostUpdate(text)
