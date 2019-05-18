from abc import ABCMeta, abstractmethod
from flask import jsonify, make_response
from result.messages import Keys


class Convertible:
    __metaclass__ = ABCMeta

    @abstractmethod
    def convert(self, dct):
        pass


class JSONConverter(Convertible):
    def convert(self, dct):
        return make_response(jsonify(dct), dct[Keys.STATUS])
