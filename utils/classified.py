from json import JSONEncoder

class ClassifiedImage(JSONEncoder):

  predict = {
    'ComFoco': 0.0,
    'SemFoco': 0.0
  }

  def __init__(self, classifier_result):
    for image in classifier_result['images']:
      for classifier in image['classifiers']:
        for classe in classifier['classes']:
          self.predict[classe['class']] = classe['score']
  @property
  def classed(self):
    return "ComFoco" if self.predict['ComFoco'] > self.predict['SemFoco'] else "SemFoco"

  @property
  def rating(self):

    return self.predict['ComFoco'] > self.predict['SemFoco']

  @property
  def score(self):
    return self.predict['ComFoco'] if self.predict['ComFoco'] > self.predict['SemFoco'] else self.predict['SemFoco']

