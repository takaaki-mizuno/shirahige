# -*- encoding:utf-8 -*-

import posixpath
import urlparse
import hashlib


class Url:
    def __init__(self, url, base=None):
        self.original = url
        (self.scheme, self.netloc, self.path, self.params, self.query, self.fragment) = urlparse.urlparse(url)
        if base:
            self.base_url = base
        else:
            self.base_url = self.base()
        self.netloc = self.netloc.lower()
        self.scheme = self.scheme.lower()

    def _sorted_query_string(self):
        if self.query:
            query = self.query.split("&")
            query.sort()
            return "&".join(query)
        return None

    def canonical(self, keep_fragments=False):
        query = self._sorted_query_string()
        path = self.path
        if path == "":
            path = "/"
        end_path = path.endswith('/')
        path = posixpath.normpath(path)
        if end_path and not path.endswith('/'):
            path += "/"
        fragment = self.fragment
        if not keep_fragments:
            fragment = ""
        return urlparse.urlunparse((self.scheme, self.netloc, path, self.params, query, fragment))

    def absolute(self, keep_fragments=False):
        url = self.canonical(keep_fragments)
        return urlparse.urljoin(self.base_url, url)

    def base(self):
        url = self.canonical()
        return urlparse.urljoin(url, "./")

    def is_only_fragment(self):
        if self.original.startswith("#"):
            return True
        return False

    def extension(self, default_extension="html"):
        filename = self.path.rsplit("/", 1)[-1]
        extension = ""
        try:
            extension = filename.rsplit(".", 1)[1]
        except IndexError:
            pass
        if extension == "":
            return default_extension
        return extension.lower()

    def hash(self):
        m = hashlib.md5()
        m.update(self.canonical())
        return m.hexdigest()

    def hash_filename(self):
        return self.hash() + "." + self.extension()
