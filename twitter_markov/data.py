"""Data gathering module
"""

import twitter

class DataPool(object):

    def get_training_data(self):
        raise NotImplemented



def TrendingTwitterPool(DataPool):

    def __init__(self, client_id, client_secret,
                 access_token_key, access_token_secret):
        self.twitter = twitter.Api(
            consumer_key = client_id,
            consumer_secret = client_secret,
            access_token_key = access_token_key,
            access_token_secret = access_token_secret)

    def get_training_data(self):
        current_trends = self.twitter.GetTrendsCurrent()
        
