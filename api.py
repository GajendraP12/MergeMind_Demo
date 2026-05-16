from flask import Flask, request
from payment_service import process_payment
from auth import verify_user

app = Flask(_name_)

@app.route("/checkout", methods=["POST"])
def checkout():

    data = request.json

    user = verify_user(data["token"])

    amount = float(data["amount"])

    result = process_payment(
        user["id"],
        amount
    )

    return {"status": result}