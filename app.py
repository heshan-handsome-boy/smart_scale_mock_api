from flask import Flask
from feature.garbage import garbage

app = Flask(__name__)

app.register_blueprint(garbage.garbage_blue_print)

if __name__ == '__main__':
    app.run()
