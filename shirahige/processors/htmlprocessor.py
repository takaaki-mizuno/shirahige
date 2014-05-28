# -*- encoding:utf-8 -*-

from shirahige.processors.baseprocessor import BaseProcessor
from shirahige.utilities import Url
from lxml import etree


class HTMLProcessor(BaseProcessor):

    def process(self):
        BaseProcessor.process(self)
        doc = etree.fromstring(self.response.text.encode('utf-8'), parser=etree.HTMLParser())
        self._replace_link(doc)
        self._replace_css(doc)
        self._remove_script(doc)
        self.result = etree.tostring(doc, pretty_print=True)

    def _replace_link(self, doc):
        for link in doc.xpath("//a"):
            href = link.get("href")
            if href:
                url = Url(href, self.url.absolute())
                if url.absolute() == self.url.absolute():
                    if url.fragment != "":
                        link.set("href", "#" + url.fragment)
                    else:
                        link.set("href", "")
                elif url.absolute().startswith(self.app.start_url.absolute()):
                    print "inner:" + href
                    link.set("href", url.hash_filename())
                    self.app.queue.add(url)
                else:
                    link.set("href", url.absolute())

    def _replace_css(self, doc):
        for link in doc.xpath('//link[@rel="stylesheet"]'):
            href = link.get("href")
            if href:
                url = Url(href, self.app.start_url.base())
                link.set("href", url.hash_filename())
                self.app.queue.add(url)

    def _remove_script(self, doc):
        for script in doc.xpath('//script'):
            print script
            doc.remove(script)
