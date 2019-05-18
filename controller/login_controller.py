#!/usr/bin/env python
# -*- coding: utf-8 -*-
from passlib.hash import pbkdf2_sha256
import pymongo
import result
from controller import BaseController
from result.messages import HttpStatus
from result.messages import Keys
from result.wrong_pass_or_phone_number import WrongPassOrPhoneNumber
from result.success_login import SuccessLogin

# logger = global_logger



class LoginController(BaseController):
    def __init__(self, login, converter):
        self.login = login
        self.converter = converter

    def execute(self):
        authentication_result = self._authentication()
        if not authentication_result[0]:
            dct_result = authentication_result[1].dictionary_creator()
            return self.serialize(dct_result, converter=self.converter)

        _, authentication_user = authentication_result

        # params = {Keys.NAME: authentication_user.name, Keys.ID: authentication_user.id}
        # Keys.NAME: authentication_user['phone_number']
        params = {Keys.ID: authentication_user['phone_number']}
        success_login = SuccessLogin(status=HttpStatus.OK, message=Keys.LOGIN_SUCCESS, params=params)
        dct_result = success_login.dictionary_creator()
        # self.add_new_key_to_session(Keys.USER_ID, authentication_user.id)
        self.add_new_key_to_session(Keys.PHONE_NUMBER, authentication_user['phone_number'])
        return self.serialize(dct_result, converter=self.converter)

    def _authentication(self):
        client = pymongo.MongoClient("localhost", 27017)
        mydb = client.admin
        find_result =  mydb.user.find({"phone_number":self.login.phone_number, "password" :self.login.password,"validate":"True"})

        # if not find_result[0]:
        #     return find_result

        if find_result.count() == 0:
            params = {Keys.PHONE_NUMBER: self.login.phone_number}
            fail = WrongPassOrPhoneNumber(status=HttpStatus.NOT_FOUND, message=result.wrong_pass_or_phone_number,
                                          params=params)
            return False, fail
        # age do ta peyda kar?
        find_result = list(find_result)
        # verified_pass = pbkdf2_sha256.verify(self.login.password, find_result[0]["password"])
        # if not verified_pass:
        if not find_result[0]["password"] == self.login.password:
            params = {Keys.PHONE_NUMBER: self.login.phone_number}
            fail = WrongPassOrPhoneNumber(status=HttpStatus.NOT_FOUND, message=Keys.WRONG_PHONE_NUMBER_OR_PASSWORD,
                                          params=params)
            return False, fail

        if not find_result[0]['code'] == self.login.code:
            params = {Keys.CODE: self.login.code}
            fail = WrongPassOrPhoneNumber(status=HttpStatus.NOT_FOUND, message=Keys.WRONG_PHONE_NUMBER_OR_PASSWORD,
                                          params=params)
            return False, fail

        return True, find_result[0]
