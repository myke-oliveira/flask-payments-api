from flask import Flask, jsonify
from repository.database import db
from models.payment import Payment

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = "your_secret_key"

db.init_app(app)

@app.route("/payments/pix", methods=["POST"])
def create_payment_pix():
    return jsonify({"message": "The payment has been created."})

@app.route("/payments/pix/confirmation", methods=["POST"])
def create_payment():
    return jsonify({"message": "The payment has been confirmed."})

@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_page(payment_id):
    return 'Pix payment'

if __name__ == "__main__":
    app.run(debug=True)
