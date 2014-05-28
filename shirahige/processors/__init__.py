# -*- encoding:utf-8 -*-

from shirahige.processors.htmlprocessor import HTMLProcessor
from shirahige.processors.cssprocessor import CSSProcessor
from shirahige.processors.binaryprocessor import BinaryProcessor
from shirahige.utilities.mimetype import MimeType


def get_processor(url, response, app):
    mimetype = MimeType(response.content_type, url)
    print "MIME:" + mimetype.type
    if mimetype.type == "html":
        return HTMLProcessor(response, url, app)
    elif mimetype.type == "css":
        return CSSProcessor(response, url, app)
    else:
        return BinaryProcessor(response, url, app)
