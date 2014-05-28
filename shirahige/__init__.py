# -*- encoding:utf-8 -*-

from shirahige.http.queue import Queue
from shirahige.http.response import Response
from shirahige.utilities import Url
from shirahige.processors import get_processor


class Shirahige():

    default_conf = {
        "save_path": "./result/"
    }

    def __init__(self, start_url, config={}):
        self.queue = Queue(self)
        self.start_url = Url(start_url)
        self.config = {}
        for key in self.default_conf.keys():
            self.config[key] = self.default_conf[key]
        for key in config.keys():
            self.config[key] = config[key]

    def run(self):
        self.queue.add(self.start_url)
        while len(self.queue) > 0:
            url = self.queue.next()
            print "Fetching :" + url.absolute()
            response = Response(url)
            if 200 <= response.status_code < 300:
                processor = get_processor(url, response, self)
                processor.process()
