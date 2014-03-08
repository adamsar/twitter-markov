"""Configuration data for the app"""
import betterconfig
import os.path

import os
import logging

log = logging.getLogger(__file__)
CONFIG_FILE_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.ini')
try:
    CONFIG = betterconfig.load(CONFIG_FILE_PATH)['config']
except IOError:
    log.warn("Config file not found!")
    CONFIG = {}

def get_prop(prop_name, alternative=None):
    return CONFIG.get(prop_name, alternative)
