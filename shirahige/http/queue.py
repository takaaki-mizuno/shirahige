# -*- encoding:utf-8 -*-

from shirahige.utilities import Url


class Queue:
    def __init__(self, app):
        self.downloaded = {}
        self.queue = {}
        self.downloading = {}

    def add(self, url):
        hash_key = url.hash()
        if hash_key in self.downloaded or hash_key in self.queue or hash_key in self.downloading:
            return False
        self.queue[hash_key] = url

    def next(self):
        (hash_key, url) = self.queue.popitem()
        self.downloading[hash_key] = url
        return url

    def finished(self, url):
        hash_key = url.hash()
        self.downloaded[hash_key] = url
        del self.downloading[hash()]

    def __len__(self):
        return len(self.queue)
