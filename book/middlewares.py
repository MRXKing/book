# -*- coding: utf-8 -*-

from book.resource import PROXIES, USER_AGENTS
import random


class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        print(proxy)
        request.meta['proxy'] = 'http://%s' % proxy


class RandomUser(object):
    def process_request(self, request, spider):
        UA = random.choice(USER_AGENTS)
        request.headers.setdefault('User-Agent', random.choice(UA))
