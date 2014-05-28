# -*- encoding:utf-8 -*-

from shirahige.processors.baseprocessor import BaseProcessor
import cssutils


class CSSProcessor(BaseProcessor):

    def process(self):
        super.process()
        self.result = self.self.response.text.encode('utf-8')
