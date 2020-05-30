from flask import Flask
from .feature.garbage import garbage

app = Flask(__name__)

app.register_blueprint(garbage, url_prefix='/garbage')

if __name__ == '__main__':
    app.run()
