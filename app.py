from flask import Flask
from routes.inventory import inventory_bp

app = Flask(__name__)
app.register_blueprint(inventory_bp, url_prefix="/inventory")

if __name__ == "__main__":
    app.run(debug=True)
