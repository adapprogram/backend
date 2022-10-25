from flask import Blueprint

indexHtml = Blueprint('index', __name__)

@indexHtml.route('')
def index():
    return 'Welcome to Adapprogram'
