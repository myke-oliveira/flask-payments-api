import uuid
import qrcode
from os import path, curdir, chdir

class Pix:
    def __init__(self):
        pass
    
    def create_payment(self):
        bank_payment_id = str(uuid.uuid4())
        hash_payment = f"hash_payment_{bank_payment_id}"
        img = qrcode.make(hash_payment)
        qr_code_path = path.join(".","static", "img", f"qr_code_payment_{bank_payment_id}.png")
        img.save(qr_code_path)
        return {
            "bank_payment_id": bank_payment_id,
            "qr_code_path": f"qr_code_payment_{bank_payment_id}"
        }