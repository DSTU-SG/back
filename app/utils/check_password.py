import hashlib

from app.utils.fake_database import fake_users_db

def verify_password(plain_password, username):
    hash_pass = hashlib.sha256(plain_password.encode()).hexdigest()
    saved_pass = fake_users_db[username]["hashed_password"]
    # Здесь должна быть логика проверки хешированного пароля
    # return plain_password == "secret" and hashed_password == "fakehashedsecret"
    return hash_pass == saved_pass