#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from flask import make_response, jsonify, session

import result
from result.bad_input_format import BadInputFormat
from result.messages import HttpStatus, Keys


def bad_schema_response(params):
    bad_input = BadInputFormat(status=HttpStatus.BAD_REQUEST, message=Keys.BAD_SCHEMA, params=params)
    dct = bad_input.dictionary_creator()
    return make_response(jsonify(dct), dct["status"])


def is_request_json(request_http):
    return request_http.is_json


def is_http_request_valid(request_http):
    return is_request_json(request_http)


def phone_number_regex_checker(phone_number):
    if re.match(r'09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}', phone_number):
        return True,
    else:
        return False, result.messages.FailKeysForJSON.phone_number_is_not_valid


def name_regex_checker(name):
    if re.match(u'^[آ-یءچ\s]{3,20}$', name):
        return True,
    else:
        return False, result.messages.FailKeysForJSON.name_is_not_valid


def password_regex_checker(password):

    if re.match(r'^ (?=.* ?[A-Z])(?=.* ?[a-z])(?=.* ?[0-9]).{6, }$', password):
        return True,
    else:
        return False, result.messages.FailKeysForJSON.password_is_not_strength

def code_validation_regex_checker(code):
    if re.match(r'^[0-9]{4}$', code):
        return True,
    else:
        return False, result.messages.FailKeysForJSON.code_pattern_is_not_valid


def unrecognized_request():
    dct = {"type": "failure", "message": "The request was not recognized.", "status": HttpStatus.BAD_REQUEST}
    return make_response(jsonify(dct), dct["status"])



def add_new_key(key, value):
    session[key] = value
