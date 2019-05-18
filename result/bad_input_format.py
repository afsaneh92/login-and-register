from result import Result
from result.messages import Keys


class BadInputFormat(Result):
    def dictionary_creator(self):
        dct = {"status": self.status, "message": Keys.BAD_SCHEMA, "params": self.params}
        return dct
