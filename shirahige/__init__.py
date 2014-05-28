# -*- encoding:utf-8 -*-

from shirahige.http.queue import Queue
from shirahige.http.response import Response
from shirahige.utilities import Url
from shirahige.processors import get_processor
import os
import os.path
import sys


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
        file_dir_path = self.get_base_path()
        if not os.path.exists(file_dir_path):
            os.makedirs(file_dir_path)
        elif os.path.isfile(file_dir_path):
            # Will Throw
            pass

    def run(self):
        self.queue.add(self.start_url)
        while len(self.queue) > 0:
            url = self.queue.next()
            print "Fetching :" + url.absolute()
            response = Response(url)
            if 200 <= response.status_code < 300:
                processor = get_processor(url, response, self)
                processor.process()
                processor.save()

    def get_base_path(self):
        base_path = self.config['save_path']
        base_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
        file_dir_path = os.path.abspath(base_dir + "/" + base_path)
        return file_dir_path
