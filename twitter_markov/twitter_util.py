"""Twitter utility methods"""

import os

from twitter_markov import config

def get_creds():
    """Returns Twitter credentials for using the API"""
    def config_or_env(config_prop, env_key):
        return config.get_prop(config_prop, os.environ.get(env_key))

    creds = map(lambda x: config_or_env(x[0], x[1]),
                (['twitter.client.key', 'TWITTER_CLIENT_KEY'],
                 ['twitter.client.secret', 'TWITTER_CLIENT_SECRET'],
                ['twitter.token.key', 'TWITTER_ACCESS_KEY'],
                ['twitter.token.secret', 'TWITTER_TOKEN_SECRET']))
    assert None not in creds, "Missing a twitter configuration option."
    return creds

def to_text(tweet):
    return tweet.text


