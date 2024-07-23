from flask import Flask, jsonify, request
from repository.database import db
from models.payment import Payment
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = "your_secret_key"

db.init_app(app)

@app.route("/payments/pix", methods=["POST"])
def create_payment_pix():
    data = request.get_json()
    
    if 'value' not in data:
        return jsonify({"message": "value field missing"}), 400
    
    expiration_date = datetime.now() + timedelta(minutes=30)
    
    new_payment = Payment(value=data.get('value'), expiration_date=expiration_date)
    
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({
        "message": "The payment has been created.",
        "payment": new_payment.to_dict()
    })

@app.route("/payments/pix/confirmation", methods=["POST"])
def create_payment():
    return jsonify({"message": "The payment has been confirmed."})

@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_page(payment_id):
    return 'Pix payment'

if __name__ == "__main__":
    app.run(debug=True)
