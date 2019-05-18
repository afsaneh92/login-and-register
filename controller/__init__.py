from abc import ABCMeta, abstractmethod

import helper


class BaseController:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

    def success_response(self, dct):
        pass

    def failure_response(self, dct):
        pass

    def serialize(self, dct, converter):
        return converter.convert(dct)

    def add_new_key_to_session(self, key, value):
        helper.add_new_key(key=key, value=value)
