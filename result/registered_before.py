from result.messages import Keys
from result import Result


class RegisteredBefore(Result):
    def dictionary_creator(self):
        return {Keys.STATUS: self.status, Keys.MESSAGE: Keys.REGISTERED_BEFORE}

