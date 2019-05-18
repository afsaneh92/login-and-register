from abc import ABCMeta, abstractmethod


class Result:
    __metaclass__ = ABCMeta



    def __init__(self, status, message=None, params=None):
        self.status = status
        self.message = message
        self.params = params

    @abstractmethod
    def dictionary_creator(self):
        pass

