from flask import Flask
from api import inventory_bp

app = Flask(__name__)

app.register_blueprint(inventory_bp)

if __name__ == "__main__":
    app.run(debug=True)