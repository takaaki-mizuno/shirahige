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
        self._replace_image(doc)
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
                    print "outer:" + href
                    link.set("href", url.absolute())

    def _replace_css(self, doc):
        for link in doc.xpath('//link[@rel="stylesheet"]'):
            href = link.get("href")
            if href:
                url = Url(href, self.url.absolute())
                print "css:" + url.absolute()
                link.set("href", url.hash_filename())
                self.app.queue.add(url)

    def _replace_image(self, doc):
        for img in doc.xpath('//img'):
            src = img.get("src")
            if src:
                url = Url(src, self.url.absolute())
                print "image:" + url.absolute()
                img.set("src", url.hash_filename())
                self.app.queue.add(url)

    def _remove_script(self, doc):
        for script in doc.xpath('//script'):
            parent = script.getparent()
            parent.remove(script)
