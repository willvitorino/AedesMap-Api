import os
import pyrebase
from dotenv import load_dotenv

load_dotenv()

__firebase_config = {
  "apiKey": os.getenv("FIREBASE_API_KEY"),
  "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
  "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
  "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
  "projectId": os.getenv("FIREBASE_PROJECT_ID"),
  "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
  "appId": os.getenv("FIREBASE_APP_ID"),
  "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID")
}
__firebase = pyrebase.initialize_app(__firebase_config)
__auth = __firebase.auth()
# user = __auth.sign_in_with_email_and_password(os.getenv("FIREBASE_ACCOUNT_EMAIL"), os.getenv("FIREBASE_ACCOUNT_PASSWORD"))
db = __firebase.database()