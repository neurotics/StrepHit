#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import absolute_import
import logging
import os
import logging.config
from urllib import unquote_plus

LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'WARN': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
}


DEFAULT_CONF = {
    'version': 1,
    'disable_existing_loggers': False,
    'loggers': {
        '': {
            'level': 'WARNING',
            'handlers': ['console', 'debug_file_handler']
        },
        'strephit': {
            'level': 'INFO',
        },
    },
    'formatters': {
        'strephit': {
            'format': '%(asctime)s [%(levelname)s] %(module)s.%(funcName)s #%(lineno)d - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'formatter': 'strephit',
            'class': 'logging.StreamHandler',
            'level': 'DEBUG'
        },
        'debug_file_handler': {
            'formatter': 'strephit',
            'level': 'DEBUG',
            'filename': 'debug.log',
            'mode': 'w',
            'class': 'logging.FileHandler',
            'encoding': 'utf8'
        }
    }
}


def setup():
    conf_path = os.path.abspath(os.path.join('dev', 'logging.ini'))
    if os.path.exists(conf_path):
        logging.config.fileConfig(conf_path, DEFAULT_CONF,
                                  disable_existing_loggers=False)
    else:
        logging.config.dictConfig(DEFAULT_CONF)


def setLogLevel(module, level):
    """ Sets the log level used to log messages from the given module """
    if level in LEVELS:
        module = '' if module == 'root' else module
        logging.getLogger(module).setLevel(level)


def log_request_data(http_response, logger):
    """
    Send a debug log message with basic information of the HTTP request that was sent for the given HTTP response.

    :param requests.models.Response http_response: HTTP response object
    """
    sent_request = {
        'method': http_response.request.method,
        'url': http_response.request.url,
        'headers': http_response.request.headers,
        'decoded_body': unquote_plus(repr(http_response.request.body))
    }
    logger.debug("Request sent: %s" % sent_request)
    return 0
