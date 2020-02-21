from flask import request
from flask_restful import Resource, reqparse

from utils.classify import classify
from utils.classified import ClassifiedImage
from utils import firebase_db as fire

class Location(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('urlImage', type=str)
    atributos.add_argument('latitude', type=float)
    atributos.add_argument('longitude', type=float)

    def get(self):
        doc = fire.db.child("locations").get().val()
        result = dict(doc).values() if doc else []
        # print(result)
        return list(result)

    def post(self):
        body = Location.atributos.parse_args()
        positivo_score = 0.0
        negativo_score = 0.0
        result = ClassifiedImage(classify(body.urlImage))
        
        data = {
            'classed': result.classed,
            'score': result.score,
            'rating': result.rating,
            'latitude': body.latitude,
            'longitude': body.longitude,
            'urlImage': body.urlImage
        }

        res = fire.db.child("locations").push(data)

        return fire.db.child("locations").get().val()[res['name']]
        # return Location.atributos.parse_args(), 200
