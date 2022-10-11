from flask import Flask
from firebase_admin import credentials,initialize_app
from flask_cors import CORS
cred = credentials.Certificate("api/key.json")
default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='12345rtfescdvf'
    CORS(app)
    from .youtubeAPI import youtubeAPI
    app.register_blueprint(youtubeAPI, url_prefix='/video')

    from .questionAPI import questionAPI
    app.register_blueprint(questionAPI, url_prefix='/question')

    from .kinesticoAPI import kinesticoAPI
    app.register_blueprint(kinesticoAPI, url_prefix='/kinestico')

    return app

