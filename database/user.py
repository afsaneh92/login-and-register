from pymongo import MongoClient
import urllib.parse
username = urllib.parse.quote_plus('user')
password = urllib.parse.quote_plus('pass/word')
MongoClient('mongodb://%s:%s@127.0.0.1' % (username, password))