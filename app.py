from flask import Flask, jsonify
from flask_cors import CORS
from api import inventory_bp

app = Flask(__name__)

# Enable CORS
CORS(app)

# Register blueprint
app.register_blueprint(inventory_bp)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to the Inventory Management System API",
        "status": "API is running",
        "available_endpoints": {
            "GET All Inventory": "/inventory",
            "GET One Item": "/inventory/<id>",
            "POST New Item": "/inventory",
            "PATCH Update Item": "/inventory/<id>",
            "DELETE Item": "/inventory/<id>",
            "GET Product from OpenFoodFacts": "/product/<barcode>"
        }
    })

if __name__ == "__main__":
    app.run(debug=True)