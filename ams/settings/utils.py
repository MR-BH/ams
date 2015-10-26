#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
from . import AMS_REDIS_SETTINGS

cache = redis.StrictRedis(host=AMS_REDIS_SETTINGS['host'],
                          port=AMS_REDIS_SETTINGS['port'],
                          db=AMS_REDIS_SETTINGS['db'])
