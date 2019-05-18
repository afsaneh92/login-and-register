from flask import Flask, Blueprint
from app import app

authentication = Blueprint('authentication', __name__)

app.register_blueprint(authentication)


@app.teardown_appcontext
def shutdown_session(exception=None):
    pass


if __name__ == '__main__':
    app.run(host="0.0.0.0")
