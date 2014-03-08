Twitter Markov Chain Tweeter
============================

Publishes a tweet that is generated randomly via a markov chain using 
trending topics once every two hours. Depends on celery for scheduling

Usage:

`celery worker --beat`