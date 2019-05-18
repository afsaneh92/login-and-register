#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from flask import json, session
from app import app
# from config import DataBaseConfig
from result.messages import HttpStatus
from result.messages import Keys
from router import authentication


class MyTestCase(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.register_blueprint(authentication)
        self.app = app.test_client()

    # executed after each test
    def tearDown(self):
        pass

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def make_post_request(self, data):
        res = self.app.post("/register_user", data=data,
                            content_type=Keys.APPLICATION_CONTENT_TYPE_JSON)
        return res

    def test_bad_schema_invalid_params_missing_in_json(self):
        data = {
            Keys.PHONE_NUMBER: "32113222222",
            Keys.PASSWORD: "Amish1234",
            Keys.NAME: "ابببسیسث",
            Keys.ADDRESS: "تهران خیابان شهید بهشتی"
        }
        data = json.dumps(data)
        response = self.make_post_request(data)
        dct = json.loads(response.data)
        self.assertEqual(dct[Keys.STATUS], HttpStatus.BAD_REQUEST)
        # self.assertEqual(dct[Keys.PARAMS], Result.language.MISSING_BUSINESS_LICENSE_IN_JSON)
        self.assertEqual(dct[Keys.MESSAGE], HttpStatus.BAD_SCHEMA)

    def test_bad_schema_invalid_params(self):
        data = {
            Keys.PHONE_NUMBER: "09124343449",
            Keys.NAME: "ابببسیسث",
            Keys.PASSWORD: "khsss",
            Keys.ADDRESS: "تهران خیابان شهید بهشتی",
        }
        data = json.dumps(data)
        response = self.make_post_request(data)
        dct = json.loads(response.data)
        self.assertEqual(dct[Keys.STATUS], HttpStatus.BAD_REQUEST)
        self.assertEqual(dct[Keys.PARAMS],  {u'invalid_params': [u'password_is_not_strength']})
        self.assertEqual(dct[Keys.MESSAGE], HttpStatus.BAD_SCHEMA)

    def test_supplier_registration_registered_validate_true(self):
        data = {
            Keys.PHONE_NUMBER: "09125200112",
            Keys.PASSWORD: "Amish1234",
            Keys.NAME: "افسانه",
            Keys.ADDRESS: "تهران خیابان شهید بهشتی",
        }

        data = json.dumps(data)
        with self.app as client:
            with client.session_transaction() as sess:
                sess['user_id'] = 13
            data = json.dumps(data)
            response = self.make_post_request(data)
            dct = json.loads(response.data)
            self.assertEqual(dct[Keys.STATUS], HttpStatus.NOT_FOUND)
            # self.assertEqual(dct[Keys.PARAMS],'taghavi')
            self.assertEqual(dct[Keys.MESSAGE], HttpStatus.REGISTERED_BEFORE)

    def test_add_user_true(self):
        data = {
            Keys.PHONE_NUMBER: "09125200115",
            Keys.PASSWORD: "Amish1234",
            Keys.NAME: "امیر",
            Keys.ADDRESS: "asssss",
        }
        json_obj = json.dumps(data)
        response = self.make_post_request(json_obj)
        dct = json.loads(response.data)
        self.assertEqual(dct[Keys.STATUS], HttpStatus.OK)
        # self.assertEqual(dct[Keys.PARAMS], 14)
        self.assertEqual(dct[Keys.MESSAGE], HttpStatus.SUCCESS_ADD_NEW_USER)

    def test_success_update_user(self):
        data = {
            Keys.PHONE_NUMBER: "09125200111",
            Keys.PASSWORD: "Amish1234",
            Keys.NAME: "امیر",
            Keys.ADDRESS: "asssss",
        }
        json_obj = json.dumps(data)
        response = self.make_post_request(json_obj)
        dct = json.loads(response.data)
        self.assertEqual(dct[Keys.STATUS], HttpStatus.OK)
        # self.assertEqual(dct[Keys.PARAMS], 14)
        # self.assertEqual(dct[Keys.MESSAGE], Result.language.SUCCESS_UPDATE)


if __name__ == '__main__':
    unittest.main()
