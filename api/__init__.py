from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    from .index import indexHtml
    app.register_blueprint(indexHtml, url_prefix='/')

    from .youtubeAPI import youtubeAPI
    app.register_blueprint(youtubeAPI, url_prefix='/video')

    from .AuditivoAPI import AuditivoAPI
    app.register_blueprint(AuditivoAPI, url_prefix='/video')

    from .questionAPI import questionAPI
    app.register_blueprint(questionAPI, url_prefix='/question')

    from .kinesticoAPI import kinesticoAPI
    app.register_blueprint(kinesticoAPI, url_prefix='/video')

    return app
