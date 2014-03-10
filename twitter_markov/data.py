"""Data gathering module
"""

from twitter_markov import twitter_util
import re

url_reg = re.compile("http(s)?://t\.co/\w+")
tweetback_reg = re.compile("@[a-zA-Z0-9]+")
hashtag_reg = re.compile("#[a-zA-Z0-9]")

class DataPool(object):

    def get_training_data(self):
        raise NotImplemented


class TrendingTwitterPool(DataPool):

    def __init__(self, twitter):
        self.twitter = twitter

    def get_training_data(self):
        current_trends = self.twitter.GetTrendsCurrent()
        tweets = map(twitter_util.to_text,
                   reduce(lambda x, y: x + y,
                        map(lambda trend: self.twitter.GetSearch(term=trend.name,
                                                                 lang='en'), current_trends)))
        for reg in (url_reg, tweetback_reg, hashtag_reg):
            tweets = [reg.sub("", tweet) for tweet in tweets]
        return " ".join(tweets)
