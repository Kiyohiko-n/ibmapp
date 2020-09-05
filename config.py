import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    UPLOAD_FOLDER = "image-file"
    CSRF_ENABLED = True
    DEBUG = False
    
    # Enter your API Key and Custom Classifier ID below
    API_KEY = "HvLj4AWOG68gwR3du9iqdiN_WthhLtQa-iYxv2YASXap"
    CLASSIFIER_ID = "helmetclassifier_1065958047"
