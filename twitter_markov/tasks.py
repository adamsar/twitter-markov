"""Celerybeat tasks"""

from celery.decorators import periodic_task
from celery.task.schedules import crontab

from twitter_markov import twitter_util, data
from twitter_markov.markov import generate_text
import twitter

@periodic_task(run_every=crontab(hour="*/2", minute="0", day_of_week="*"))
def tweet_latest():
    key, secret, akey, asecret = twitter_util.get_creds()
    client = twitter.Api(
        consumer_key = key,
        consumer_secret = secret,
        access_token_key = akey,
        access_token_secret = asecret)
    seed_words = data.TrendingTwitterPool(client).get_training_data()
    text = generate_text(seed_words, initial_model=1000)
    client.PostUpdate(text)

