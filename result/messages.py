#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum


class HttpStatus(Enum):
    """
    https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
    """
    INTERNAL_ERROR = 500  # done
    BAD_REQUEST = 400  # done
    ACCESS_FORBIDDEN = 403
    NOT_FOUND = 404  # done
    OK = 200

class Keys:
    ADDRESS = "address"
    CODE = "code"
    REG_ID = 'reg_id'
    USER_ID = 'user_id'
    ID = 'id'
    NAME = 'name'
    METHOD_GET = 'GET'
    METHOD_PUT = 'PUT'
    METHOD_DELETE = 'DELETE'
    METHOD_UPDATE = 'UPDATE'
    METHOD_POST = 'POST'

    PARAMS = 'params'
    MESSAGE = 'message'
    STATUS = 'status'

    PHONE_NUMBER = "phone_number"
    PASSWORD = "password"
    LOGIN_SUCCESS = "login success"
    WRONG_PHONE_NUMBER_OR_PASSWORD = "wrong password or phone number"
    APPLICATION_CONTENT_TYPE_JSON = "application content type is json"
    REGISTERED_BEFORE = "registered_before"
    BAD_SCHEMA = "bad schema"

class FailKeysForJSON:
    username_is_empty = "username_is_empty"
    password_is_empty = "password_is_empty"
    phone_number_is_empty = "phone_number_is_empty"
    car_owner_registered_before = "car_owner_registered_before"
    missing_password_in_json = "missing_password_in_json"
    missing_name_in_json = "missing_name_in_json"
    missing_phone_number_in_json = "missing_phone_number_in_json"
    missing_code_validation_in_json = "missing_code_validation_in_json"
    password_is_not_strength = "password_is_not_strength"
    phone_number_is_not_valid = "phone_number_is_not_valid"
    name_is_not_valid = "name_is_not_valid"
    code_pattern_is_not_valid = "code_pattern_is_not_valid"
    input_pattern_is_not_valid = "input_pattern_is_not_valid"
    request_is_not_json = "request_is_not_json"
    user_has_registered_before = "user_has_registered_before"
    number_pattern_is_not_valid = "number_pattern_is_not_valid"
