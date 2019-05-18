import logging
from datetime import timedelta
from logging import config

from flask import Flask

app = Flask(__name__)

app.secret_key = u'=\xad\xc5\xbb\xe4\xb5\xed\x8at\xfb\x14\x1c\xfei\xd9IpG|\xf1\rMd\x89'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['LOGGER_HANDLER_POLICY'] = 'always'  # 'always' (default), 'never',  'production', 'debug'
app.config['LOGGER_NAME'] = 'login_logger'  # define which logger to use for Flask
app.permanent_session_lifetime = timedelta(minutes=6 * 30 * 24 * 60)
_ = app.logger  # initialise logger
# db = SQLAlchemy(app)

logging.basicConfig(level=logging.INFO)
# config.dictConfig(LoggerConfig.dictConfig)
global_logger = logging.getLogger(app.logger.name)
