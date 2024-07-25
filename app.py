from flask import Flask, jsonify, request, send_file, render_template
from repository.database import db
from models.payment import Payment
from datetime import datetime, timedelta
from payments.pix import Pix

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
    
    pix = Pix()
    data_payment_pix = pix.create_payment()
    new_payment.bank_payment_id = data_payment_pix["bank_payment_id"]
    new_payment.qr_code = data_payment_pix["qr_code_path"]
    
    db.session.add(new_payment)
    db.session.commit()
    
    return jsonify({
        "message": "The payment has been created.",
        "payment": new_payment.to_dict()
    })
    
@app.route("/paymens/pix/qr_code/<filename>", methods=["GET"])
def get_image(filename):
    return send_file(f"static/img/{filename}.png", mimetype="image/png")

@app.route("/payments/pix/confirmation", methods=["POST"])
def pix_confirmation():
    return jsonify({"message": "The payment has been confirmed."})

@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_page(payment_id):
    return render_template("payment.html")

if __name__ == "__main__":
    app.run(debug=True)
