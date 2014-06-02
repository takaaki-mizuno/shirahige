# -*- encoding:utf-8 -*-

from shirahige.processors.baseprocessor import BaseProcessor
from shirahige.utilities import Url
import cssutils
import logging

class CSSProcessor(BaseProcessor):

    def process(self):
        BaseProcessor.process(self)
        cssutils.log.setLevel(logging.CRITICAL)
        css = cssutils.parseString(self.response.text.encode('utf-8'))
        self._replace_url(css)
        self.result = css.cssText

    def _replace_url(self, css):
        for rule in css:
            if rule.type == rule.MEDIA_RULE:
                self._replace_url(rule)
            elif rule.type == rule.STYLE_RULE:
                for prop in rule.style:
                    for value in prop.propertyValue:
                        if isinstance(value, cssutils.css.URIValue):
                            url = Url(value.uri, self.url.absolute())
                            value.uri = url.hash_filename()
                            self.app.queue.add(url)
#                        else:
#                            print value

