from flask import Flask, Blueprint
from flask import request
from controller.login_controller import LoginController
from controller.registeration_controller import UserRegistrationController
from convertor import JSONConverter
from helper import bad_schema_response, is_http_request_valid, unrecognized_request
from request.login_request import LoginRequest
from request.registeration_request import UserRegistrationRequest


authentication = Blueprint('authentication', __name__)


@authentication.route('/')
def hello_world():
    return 'Hello World!'


@authentication.route('/login', methods=["POST"])
def login_func():

    # if not is_http_request_valid(request.data):
    #     return unrecognized_request()

    result = LoginRequest(request.data)
    deserialize_result = result.deserialize()
    if not deserialize_result[0]:
        return bad_schema_response(deserialize_result[1])

    converter = JSONConverter()
    login_controller = LoginController(deserialize_result[1], converter)
    ret = login_controller.execute()
    return ret

@authentication.route('/register_user', methods=["POST"])
def register_user_func():

    # if not is_http_request_valid(request):
    #     return unrecognized_request()

    user = UserRegistrationRequest(request.data)
    deserialize_result = user.deserialize()
    if not deserialize_result[0]:
        return bad_schema_response(deserialize_result[1])

    converter = JSONConverter()
    user_controller = UserRegistrationController(deserialize_result[1], converter)
    ret = user_controller.execute()
    return ret
