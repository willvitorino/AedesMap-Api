from flask import request
from flask_restful import Resource, reqparse

class Home(Resource):
  def get(self):
    return {}