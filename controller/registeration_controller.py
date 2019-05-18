import pymongo
from app import global_logger
from controller import BaseController
from result.messages import Keys, HttpStatus
from result.registered_before import RegisteredBefore
from result.success_registered import SuccessRegistered
from services import CodeValidationChannel, SMSCodeValidation

logger = global_logger

class UserRegistrationController(BaseController):

    def __init__(self, user, converter):
        self.user = user
        self._random_code = CodeValidationChannel.create_random_code()
        self.converter = converter

    def execute(self):
        result = self._add_new_user_record()
        if not result[0]:
            dct = result[1].dictionary_creator()
            return self.serialize(dct, converter=self.converter)

        code_valid_result = self._send_validation_code()
        # if not code_valid_result[0]:
        #     logger.warning('code has not been send to user:' + self.user.phone_number, exc_info=True)
        params = {Keys.ID: self.user.phone_number}
        success_registered = SuccessRegistered(status=HttpStatus.OK, message=Keys.LOGIN_SUCCESS, params=params)
        dct = success_registered.dictionary_creator()
        return self.serialize(dct, converter=self.converter)

    def _add_new_user_record(self):
        result = True,
        client = pymongo.MongoClient("localhost", 27017)
        mydb = client.admin
        find_result = mydb.user.find({"phone_number": self.user.phone_number, "password": self.user.phone_number
          ,"validate":"True"})
        find_result_2 = mydb.user.find({"phone_number": self.user.phone_number, "password": self.user.phone_number,"validate":"False"})

        if find_result.count():
            params = {"name": self.user.name}
            registered_before = RegisteredBefore(status=404, message=Keys.REGISTERED_BEFORE, params=params)
            return False, registered_before
        elif find_result_2.count():
            dct = {"code": str(self._random_code)}
            # result = mydb.user.update({'phone_number':self.user.phone_number},
            #         {$set:{'code':dct}},{multi:true}))
        else:
            code = str(self._random_code)
            result = mydb.user.insert({"phone_number": self.user.phone_number, "password": self.user.phone_number,"validate":"True","code":code, "address":self.user.address, "name":self.user.name})

        return True,result

    def _send_validation_code(self):
        sms = SMSCodeValidation(self.user.name, self.user.phone_number, self._random_code)
        result = sms.send_validation_code()
        return result

