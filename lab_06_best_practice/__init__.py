from lab_06_best_practice.app.views import bp as controllers
from flask import Flask
app = Flask(__name__)
app.register_blueprint(controllers)
