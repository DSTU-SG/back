import hashlib

hash_obj = hashlib.sha256()
byte_pass = "fakehashedsecret".encode()
hash_obj.update(byte_pass)
hex_pass = hash_obj.hexdigest()

fake_users_db = {
    1: {
        "username": "johndoe",
        "hashed_password": hex_pass,
    }
}

cards = {
    1: {
        "number": 11111111111,
    }
}