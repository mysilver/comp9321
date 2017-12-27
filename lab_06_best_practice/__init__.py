from lab_08_authentication.app.views import bp as controllers
from flask import Flask
app = Flask(__name__)
app.register_blueprint(controllers)
