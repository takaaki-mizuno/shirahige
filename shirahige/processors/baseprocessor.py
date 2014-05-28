# -*- encoding:utf-8 -*-

import os.path
from shirahige.utilities.url import Url


class BaseProcessor():

    def __init__(self, response, url, app):
        self.app = app
        self.url = url
        self.response = response
        self.result = None

    def process(self):
        pass

    def save(self):
        path = self.app.config['save_path']
        base_dir = os.path.dirname(os.path.realpath(__file__))
        file_path = base_dir + "/" + path + "/" + self.url.hash_filename()
        fh = open('Failed.py', 'wb')
        fh.write(self.result)
        fh.close()
