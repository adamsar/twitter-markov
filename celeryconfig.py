CELERY_IMPORTS = ("twitter_markov.tasks",)

BROKER_BACKEND = "sqlakombu.transport.Transport"
BROKER_URL = 'sqla+sqlite:///celerydb.sqlite'
