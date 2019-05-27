from flask import Flask, Blueprint
import routes

bp = Blueprint('routes', __name__)

def createApp():
    app = Flask(__name__)
    app.register_blueprint(routes.allRoutes.bp)
    app.debug = True
    return app
    