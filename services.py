from abc import abstractmethod, ABCMeta
import random


class CodeValidationChannel:
    __metaclass__ = ABCMeta
    name = ""
    destination = ""
    message = ""

    def __init__(self, name, destination, message):
        pass

    @abstractmethod
    def send_validation_code(self):
        pass

    @abstractmethod
    def create_validation_code(self):
        pass

    @staticmethod
    def create_random_code():
        return random.randint(1000, 10000)


class SMSCodeValidation(CodeValidationChannel):
    def __init__(self, name, destination, code):
        self.name = name
        self.destination = destination
        self.code = code
        # self.user_id = user_id
