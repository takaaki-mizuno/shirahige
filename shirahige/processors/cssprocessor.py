# -*- encoding:utf-8 -*-

from shirahige.processors.baseprocessor import BaseProcessor
from shirahige.utilities import Url
import cssutils


class CSSProcessor(BaseProcessor):

    def process(self):
        BaseProcessor.process(self)
        css = cssutils.parseString(self.response.text.encode('utf-8'))
        self._replace_url(css)
        self.result = css.cssText

    def _replace_url(self, css):
        for rule in css:
            if rule.type == rule.STYLE_RULE:
                for p in rule.style:
                    if isinstance(p.value,cssutils.css.URIValue):
                        url = Url(p.value.uri, self.url.absolute())
                        print "css inside:" + url.absolute()
                        p.value.uri = url.hash_filename()
                        self.app.queue.add(url)
