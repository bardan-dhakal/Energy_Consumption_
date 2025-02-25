from flask import Flask
from flask_cors import CORS
from config import Config
from routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)