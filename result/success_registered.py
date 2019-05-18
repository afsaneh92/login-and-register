from result.messages import Keys
from result import Result


class SuccessRegistered(Result):
    def dictionary_creator(self):
        return {Keys.STATUS: self.status, Keys.MESSAGE: self.message,
                Keys.PARAMS: self.params}
