from flask import Flask
from feature.garbage import garbage

app = Flask(__name__)

app.register_blueprint(garbage.garbage_blue_print)


@app.route('/')
def root():
    return 'Hello world smart scale mock api'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
