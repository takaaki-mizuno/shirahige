# -*- encoding:utf-8 -*-

from shirahige.utilities import Url
from dotdict import DotDict


class MimeType:
    extension_map = {
        'htm'  : { 'type': 'html',  'ext': 'html' },
        'html' : { 'type': 'html',  'ext': 'html' },
        'xml'  : { 'type': 'file',  'ext': 'xml'  },
        'rss'  : { 'type': 'file',  'ext': 'xml'  },
        'css'  : { 'type': 'css',   'ext': 'css'  },
        'js'   : { 'type': 'js',    'ext': 'js'   },
        'gif'  : { 'type': 'image', 'ext': 'gif'  },
        'png'  : { 'type': 'image', 'ext': 'png'  },
        'jpg'  : { 'type': 'image', 'ext': 'jpg'  },
        'jpeg' : { 'type': 'image', 'ext': 'jpg'  },
    }

    content_types = {
        'text': {
            'html'       : { 'type': 'html', 'ext': 'html' },
            'xml'        : { 'type': 'file', 'ext': 'xml'  },
            'css'        : { 'type': 'css',  'ext': 'css'  },
            'plain'      : { 'type': 'file', 'ext': 'txt'  },
            'javascript' : { 'type': 'js',   'ext': 'js'   },
            'rtf'        : { 'type': 'file', 'ext': 'rtf'  },
            'default'    : { 'type': 'file', 'ext': 'html' },
        },
        'application': {
            'pdf'        : { 'type': 'file', 'ext': 'pdf'  },
            'javascript' : { 'type': 'js',   'ext': 'js'   },
            'json'       : { 'type': 'file', 'ext': 'json' },
            'xml'        : { 'type': 'file', 'ext': 'xml'  },
            'default'    : { 'type': 'file', 'ext': ''     },
        },
        'image': {
            'gif'        : { 'type': 'image', 'ext': 'gif'  },
            'png'        : { 'type': 'image', 'ext': 'png'  },
            'tiff'       : { 'type': 'image', 'ext': 'tiff' },
            'jpeg'       : { 'type': 'image', 'ext': 'jpg'  },
            'default'    : { 'type': 'file',  'ext': ''      },
        },
        'default': {
            'default'    : { 'type': 'file', 'ext': 'html' },
        }
    }

    def __init__(self, content_type, url):
        self.content_type = content_type
        self.url = url
        res = self._detect_file_type()
        self.type = res['type']
        self.ext = res['ext']

    def _parse_content_type(self):
        content_type = self.content_type.split(";",1)[0]
        types = content_type.split("/",1)
        if len(types) == 2:
            try:
                main = types[0].lower()
                sub  = types[1].lower()
                if sub.find('+') > -1:
                    sub = sub.rsplit("+")[-1]
                return main, sub
            except:
                pass
        return None, None

    def _detect_file_type(self):
        (main, sub) = self._parse_content_type()
        result = self.content_types['default']['default']
        if main in self.content_types and sub in self.content_types[main]:
            result = self.content_types[main][sub]
        else:
            ext = self.url.extension()
            if ext in self.extension_map:
                result = self.extension_map[ext]
            elif main in self.content_types:
                result = self.content_types[main]['default']
        return result
