from lab_02_Blueprints.app.views import bp as controllers
from flask import Flask
app = Flask(__name__)
app.register_blueprint(controllers)
