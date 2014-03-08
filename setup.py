from setuptools import setup, find_packages

# To install the twilio-python library, open a Terminal shell, then run this
# file by typing:
#
# python setup.py install
#
# You need to have the setuptools module installed. Try reading the setuptools
# documentation: http://pypi.python.org/pypi/setuptools
setup(
    name = "twitter-markov",
    version = "0.1",
    description = "Generator for twitter content using trending tweets and markov chains",
    author = "Andrew Adams",
    author_email = "adamsar@gmail.com",
    url = "https://github.com/adamsar/twitter-markov",
    keywords = ["python", "twitter", "markov"],
    install_requires = [
        'python-twitter',
        'nltk',
        'betterconfig',
        'celery',
        'kombu-sqlalchemy'
    ],
    include_package_data=True,
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Awesome stuff",
        ]
    )
