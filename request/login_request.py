from helper import password_regex_checker, phone_number_regex_checker, code_validation_regex_checker
from serialize import Serializable


class LoginRequest:
    def __init__(self, json_obj):
        self.json_obj = json_obj


    def validate_pattern(self):
        invalid_params = []

        result = self._password_checker(self.password)
        if not result[0]:
            invalid_params.append(result[1])
        res = self._phone_number_checker(self.phone_number)
        if not res[0]:
            invalid_params.append(result[1])
        res = self._code_validation_checker(self.code)
        if not res[0]:
            invalid_params.append(result[1])
        if len(invalid_params) > 0:
            return False, {"invalid_params": invalid_params}
        return True, "regex is valid"


    def _password_checker(self, password):
        return password_regex_checker(password)

    def _phone_number_checker(self, phone_number):
        return phone_number_regex_checker(phone_number)

    def _code_validation_checker(self, code):
        return code_validation_regex_checker(code)


    @staticmethod
    def pre_deserialize(json_dict):
        """
        before deserializing, run this method. It help to check json and confirm it's schema.
        :param json_dict:
        :return:
        """
        missed_params = []
        if 'phone_number' not in json_dict:
            missed_params.append("missing_phone_number_in_json")
        if 'password' not in json_dict:
            missed_params.append("missing_password_in_json")
        if 'code' not in json_dict:
            missed_params.append("missing_code_in_json")
        if len(missed_params) > 0:
            return False, missed_params

        return True,


    def post_deserialize(self):
        return self.validate_pattern()

    def deserialize(self):
        if not type(self.json_obj) is dict :
            json_dict = Serializable.convert_input_to_dict(self.json_obj)
        else:
            json_dict = self.json_obj
        result = LoginRequest.pre_deserialize(json_dict)
        if result[0]:
            self.phone_number = json_dict['phone_number']
            self.password = json_dict['password']
            self.code = json_dict['code']
            result_pattern = self.post_deserialize()
            if not result_pattern[0]:
                return result_pattern
            return True, self
        return result