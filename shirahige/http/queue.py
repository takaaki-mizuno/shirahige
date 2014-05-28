# -*- encoding:utf-8 -*-

from shirahige.utilities import Url


class Queue:
    def __init__(self, app):
        self.downloaded = {}
        self.queue = {}
        self.downloading = {}

    def add(self, url):
        hashkey = url.hash()
        if hashkey in self.downloaded or hashkey in self.queue or hashkey in self.downloading:
            return False
        self.queue[hashkey] = url

    def next(self):
        (hashkey, url) = self.queue.popitem()
        self.downloading[hashkey] = url
        return url

    def finished(self, url):
        hashkey = url.hash()
        self.downloaded[hashkey] = url
        del self.downloading[hash()]

    def __len__(self):
        return len(self.queue)
