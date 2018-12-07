#!/usr/bin/python

from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world-breaker-hulk'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
