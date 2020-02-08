from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_pymongo import PyMongo

# Acesso as Variáveis de Ambiente
import os
from dotenv import load_dotenv

load_dotenv()

# Configurações do Firebase

import pyrebase

firebase_config = {
  "apiKey": os.getenv("FIREBASE_API_KEY"),
  "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
  "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
  "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
  "projectId": os.getenv("FIREBASE_PROJECT_ID"),
  "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
  "appId": os.getenv("FIREBASE_APP_ID"),
  "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

firebase = pyrebase.initialize_app(firebase_config)

# Recursos da Api
from resources.location import Location

app = Flask(__name__)


# MongoDB Config
# app.config["MONGO_URI"] = os.getenv("MONGODB_URL")
# mongo = PyMongo(app)


CORS(app)
api = Api(app)

api.add_resource(Location, '/location')

if __name__ == '__main__':
    db = firebase.database()
    data = { "name": "Mortimer 'Morty' Smith" }

    app.run(debug=True)