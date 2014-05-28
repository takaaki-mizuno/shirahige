# -*- coding: utf-8 -*-

# http://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary


class DotDict(object):
    def __init__(self, d=None, create=True):
        if d is None:
            d = {}
        supr = super(DotDict, self)
        supr.__setattr__('_data', d)
        supr.__setattr__('__create', create)

    def __getattr__(self, name):
        try:
            value = self._data[name]
        except KeyError:
            if not super(DotDict, self).__getattribute__('__create'):
                raise
            value = {}
            self._data[name] = value

        if hasattr(value, 'items'):
            create = super(DotDict, self).__getattribute__('__create')
            return DotDict(value, create)
        return value

    def __setattr__(self, name, value):
        self._data[name] = value

    def __getitem__(self, key):
        try:
            value = self._data[key]
        except KeyError:
            if not super(DotDict, self).__getattribute__('__create'):
                raise
            value = {}
            self._data[key] = value

        if hasattr(value, 'items'):
            create = super(DotDict, self).__getattribute__('__create')
            return DotDict(value, create)
        return value

    def __setitem__(self, key, value):
        self._data[key] = value

    def __iadd__(self, other):
        if self._data:
            raise TypeError("A Nested dict will only be replaced if it's empty")
        else:
            return other