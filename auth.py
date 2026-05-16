import jwt

SECRET_KEY="my_company_secret"

def verify_user(token):

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )

    return {
        "id":payload["user_id"],
        "role":payload["role"]
    }