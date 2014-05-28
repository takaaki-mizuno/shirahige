# -*- encoding:utf-8 -*-

import requests


class Response:
    def __init__(self, url):
        r = requests.get(url.absolute())
        self.status_code = r.status_code
        self.content_type = r.headers['content-type']
        self.encoding = r.encoding
        self.content = r.content
        self.text = r.text
        self.filename = url.hash_filename()
