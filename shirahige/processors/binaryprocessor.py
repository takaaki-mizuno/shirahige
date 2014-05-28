# -*- encoding:utf-8 -*-

from shirahige.processors.baseprocessor import BaseProcessor


class BinaryProcessor(BaseProcessor):

    def process(self):
        super.process()
        self.result = self.self.response.content
