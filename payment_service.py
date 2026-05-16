import requests
import logging

logger=logging.getLogger()

def process_payment(user_id, amount):

    logger.info(
        f"Processing payment for {user_id}"
    )

    response=requests.post(
        "https://payment-api.company.com/pay",
        json={
            "user":user_id,
            "amount":amount
        }
    )

    return response.json()["status"]