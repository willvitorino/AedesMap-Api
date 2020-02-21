import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


import os
from dotenv import load_dotenv

load_dotenv()

authenticator = IAMAuthenticator(os.getenv("VISUAL_RECOGNITION_API_KEY"))
visual_recognition = VisualRecognitionV3( '2018-03-19', authenticator=authenticator )
visual_recognition.set_service_url(os.getenv("VISUAL_RECOGNITION_URL"))

def classify(url):
  classifier_ids = ["AedesMap-classifier_174399366"]

  return visual_recognition.classify(url=url, classifier_ids=classifier_ids).get_result()
  # return json.dumps(classes_result, indent=2)