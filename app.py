from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_pymongo import PyMongo

# Acesso as Variáveis de Ambiente
import os
from dotenv import load_dotenv

load_dotenv()

# Recursos da Api
from resources.location import Location
from resources.home import Home

app = Flask(__name__)


# MongoDB Config
# app.config["MONGO_URI"] = os.getenv("MONGODB_URL")
# mongo = PyMongo(app)


CORS(app)
api = Api(app)
api.add_resource(Home, '/')
api.add_resource(Location, '/location')

def main():
    port = int(os.environ.get("PORT", 5000))
    # Local
    # app.run(debug=True, port=5000, host='192.168.0.12')
    # Production
    app.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    main()
