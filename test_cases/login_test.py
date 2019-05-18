#!/usr/bin/env python
# -*- coding: utf-8 -*-
# login and register/test_cases

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

        # self.app.testing = True
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
        res = self.app.post("/login", data=data,
                            content_type=Keys.APPLICATION_CONTENT_TYPE_JSON)
        return res

    def test_login_true(self):
        data = {
            Keys.PHONE_NUMBER: "09125200200",
            Keys.PASSWORD: "Amish1234",
            Keys.CODE : "4422"
        }
        data = json.dumps(data)
        with self.app as client:
            response = self.make_post_request(data)
            dct = json.loads(response.data)
            self.assertEqual(dct[Keys.STATUS], HttpStatus.OK)
            self.assertEqual(session[Keys.PHONE_NUMBER], data[Keys.PHONE_NUMBER])

    def test_login_false_password(self):
        data = {
            Keys.PHONE_NUMBER: "09125200200",
            Keys.PASSWORD: "Amish12345",
            Keys.CODE : "4422"
        }
        data1 = json.dumps(data)
        with self.app as client:
            response = self.make_post_request(data1)
            dct = json.loads(response.data)
            self.assertEqual(dct[Keys.STATUS], HttpStatus.OK)
            self.assertEqual(session[Keys.PHONE_NUMBER], data[Keys.PHONE_NUMBER])

    def test_login_false_code(self):
        data = {
            Keys.PHONE_NUMBER: "09125200200",
            Keys.PASSWORD: "Amish1234",
            Keys.CODE : "4433"
        }
        data1 = json.dumps(data)
        with self.app as client:
            response = self.make_post_request(data1)
            dct = json.loads(response.data)
            self.assertEqual(dct[Keys.STATUS], HttpStatus.OK)
            self.assertEqual(session[Keys.PHONE_NUMBER], data[Keys.PHONE_NUMBER])


    def test_login_false_regex(self):
        data = {
            Keys.PHONE_NUMBER: "09125200100",
            Keys.PASSWORD: "Amish",
            Keys.CODE: "4422"
        }
        data = json.dumps(data)
        with self.app as client:
            response = self.make_post_request(data)
            dct = json.loads(response.data)
            self.assertEqual(dct[Keys.STATUS], HttpStatus.BAD_REQUEST)
            self.assertEqual(Keys.PHONE_NUMBER in session, False)

    def test_login_not_registered(self):
        data = {
            Keys.PHONE_NUMBER: "09125200113",
            Keys.PASSWORD: "Amish1234",
            Keys.CODE: "4422"
        }
        data = json.dumps(data)
        with self.app as client:
            response = self.make_post_request(data)
            dct = json.loads(response.data)
            self.assertEqual(dct[Keys.STATUS], HttpStatus.NOT_FOUND)
            self.assertEqual(Keys.PHONE_NUMBER in session, False)


if __name__ == '__main__':
    unittest.main()
