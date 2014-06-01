# -*- encoding:utf-8 -*-

from shirahige.processors.baseprocessor import BaseProcessor
import cssutils


class CSSProcessor(BaseProcessor):

    def process(self):
        BaseProcessor.process(self)
        self.result = self.response.text.encode('utf-8')
