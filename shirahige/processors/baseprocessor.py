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
        path = self.app.get_base_path()
        file_path = path + "/" + self.url.hash_filename()
        fh = open(file_path, 'wb')
        fh.write(self.result)
        fh.close()
